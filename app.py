import streamlit as st
import cv2
import numpy as np
from pyzbar import pyzbar
from sqlalchemy import text
from data_base import connect_db
# Streamlit basicão
st.set_page_config(page_title="Controle de Mudança", layout="centered")
st.title("Controle de Mudança: Fluxo de Saída")

engine = connect_db()

if engine is not None:
    
    # duas abas do stremlit para manual ou camera
    aba_camera, aba_manual = st.tabs(["Câmera", "Digitação Manual"])
    patrimonio_capturado = None

    # Opcção por camera
    with aba_camera:
        foto_capturada = st.camera_input("Tire uma foto legível do código de barras")
        if foto_capturada:
            # aqui está o segredo: código básico pra ler código barras e qrcodes
            # bytes_imagens: gera um array numpy - tabela de vetor numerico/ bytearray é nativo python
            # img: a Opencv codifica esse array para identificar a imagem
            # codigos_encontrados: essa bibl. pyzbar faz as vezes de decodificar e ler códigos de barras e qrcodes a partir.
            # de arquivos da Opencv, numpy e bytesbrutos.
            bytes_imagem = np.asarray(bytearray(foto_capturada.read()), dtype=np.uint8)
            # esse método da opencv imread_color detecta RGB da imagem, tem outros na documentação: 
            # imread_grayscale(talvez funcione até melhor e mais leve que esse que usei) e imread_unchaged
            img = cv2.imdecode(bytes_imagem, cv2.IMREAD_COLOR)

           # aqui o pyzbar retorna varios atributos, o primeiro é o principal,[0], .data . Ele faz uma varredura
        #    por gradiente, partes claras e escuras da imagem. Não é deep learning...
            codigos_encontrados = pyzbar.decode(img)
            
            if codigos_encontrados:
                patrimonio_capturado = codigos_encontrados[0].data.decode("utf-8").strip()
            else:
                st.error("Nenhum código detectado na foto. Tente aproximar mais.")

    # Opção por digitar
    with aba_manual:
        codigo_digitado = st.text_input("Digite o Número do Patrimônio:").strip()
        if codigo_digitado:
            patrimonio_capturado = codigo_digitado

    # Lógica única de Processamento Relacional no Banco de Dados
    if patrimonio_capturado:
        # :patrimonio é uma Query Parametrizada , uso um placeholder aqui e depois uso na variavel. Evita SQL injection
        query_busca = text("""
            SELECT id, equipamento, qtde_ 
            FROM equipamentos_estudio 
            WHERE n_patrimonio = :patrimonio
        """)

        
        with engine.connect() as conn:
            result = conn.execute(query_busca, {"patrimonio": patrimonio_capturado}).fetchone()
            
            if result:
                # aqui fica mais limpo usar um desempacotamento de tupla. O resultado da vaiável result é algo assim:
                # result=(42,"sony Camera x", 1), daí é só inverter e colocar o nome da chave e depois a variavel.
                id_interno, nome_equipamento, saldo_atual = result
                
                st.markdown("---")
                st.success(f"**Item:** {nome_equipamento}")
                st.write(f"**Patrimônio:** {patrimonio_capturado} | **Estoque:** {saldo_atual} un")
                
                if saldo_atual <= 0:
                    st.error("Erro: Equipamento com saldo zerado no estoque.")
                else:
                    if st.button("CONFIRMAR ENVIO", use_container_width=True, type="primary"):
                        
                        query_insercao = text("""
                            INSERT INTO saida_equipamentos (equipamento_id, qtde_saida, destino, responsavel)
                            VALUES (:id_interno, 1, 'Prédio Novo', 'Operador Web')
                        """)
                        
                        query_update_estoque = text("""
                            UPDATE equipamentos_estudio 
                            SET qtde_ = qtde_ - 1 
                            WHERE id = :id_interno
                        """)
                        # Aqui eu usei de novo a query parametrizada pra evitar sql injection
                        conn.execute(query_insercao, {"id_interno": id_interno})
                        conn.execute(query_update_estoque, {"id_interno": id_interno})
                        # Aqui o commit sobe as duas querys ou nada... evita operação pela metade
                        conn.commit()
                        
                        st.success("Movimentação registrada com sucesso.")
                        st.rerun()
            else:
                st.error(f"Código '{patrimonio_capturado}' não encontrado no banco de dados.")
