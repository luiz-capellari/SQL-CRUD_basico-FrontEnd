import pandas as pd
from data_base import connect_db


engine = connect_db()

if engine is not None:
    
    df = pd.read_excel('equipamentos_completo.xlsx')

    # Estou juntando a marca e a descrição (JOIN) na coluna equipamento
    df['Equipamento'] = df['Marca'].astype(str).str.strip() + ' - ' + df['Descricao'].astype(str).str.strip()

    
    dados_banco = pd.DataFrame({
        'equipamento': df['Equipamento'],
        'qtde_': 1, 
        'n_patrimonio': df['Codigo'].astype(str).str.strip(),
        'observacoes_': 'Carga inicial via planilha'
    })

    
    dados_banco = dados_banco.dropna(subset=['equipamento'])

    # Formato específico de configuração do sqlalquemy
    dados_banco.to_sql(
        name='equipamentos_estudio', 
        con=engine, 
        if_exists='append', 
        index=False
    )

    print(f"Sucesso! {len(dados_banco)} equipamentos foram importados para o banco de dados.")
