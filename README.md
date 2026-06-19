# Controle de Mudança de Patrimônio

Este projeto foi desenvolvido como uma ferramenta temporária para apoiar a empresa EBC no processo de mudança de sede.

A aplicação ajuda a controlar a saída de bens patrimoniais, cruzando o código lido na etiqueta com os registros armazenados no banco de dados e registrando cada movimentação de forma organizada.

## Contexto do projeto

A EBC está em processo de mudança da sede atual para um novo prédio próximo à Estação da Luz, no Centro de São Paulo.

Como se trata de uma empresa pública federal, o processo envolve conferência de patrimônio, controle de saída de equipamentos e rastreabilidade dos itens movimentados.

## Objetivo

O objetivo da aplicação é facilitar a conferência dos bens durante a mudança, reduzindo erros manuais e centralizando as informações em um banco de dados relacional.

## Funcionalidades

- Leitura de código de barras pela câmera do celular.
- Entrada manual do número do patrimônio.
- Consulta do patrimônio no banco de dados.
- Exibição do nome do equipamento e da quantidade disponível antes da baixa.
- Registro da saída do item em uma tabela específica de movimentações.
- Atualização automática do saldo do equipamento após a confirmação.
- Bloqueio de baixa quando o saldo já estiver zerado.
- Importação inicial de equipamentos a partir de planilha Excel.
- Uso de banco de dados PostgreSQL para persistência dos registros.

## Fluxo de uso

1. O usuário abre a aplicação no Streamlit.
2. Informa o patrimônio pela câmera ou digitando manualmente.
3. O sistema consulta o item no banco de dados.
4. Se o equipamento existir e houver saldo, a aplicação exibe os dados do item.
5. Ao confirmar o envio, o sistema registra a saída e reduz a quantidade disponível.

## Estrutura do projeto

- `app.py`: interface principal da aplicação no Streamlit.
- `data_base.py`: conexão com o banco de dados.
- `importar_planilha.py`: carga inicial da planilha para o banco.
- `tratamento_planilha.py`: preparação dos dados da planilha antes da importação.
- `backup.sql`: backup do banco com as tabelas principais.
- `equipamentos_completo.xlsx`: base original utilizada na carga inicial.

## Tecnologias utilizadas

- Python
- Streamlit
- PostgreSQL
- SQLAlchemy
- OpenCV
- NumPy
- Pyzbar
- Pandas
- OpenPyXL
- python-dotenv

## Banco de dados

O projeto utiliza duas tabelas principais:

- `equipamentos_estudio`: armazena os equipamentos, patrimônio, quantidade e observações.
- `saida_equipamentos`: registra as saídas realizadas durante a mudança.

O arquivo `backup.sql` pode ser usado como base para recriar a estrutura do banco.

## Propostas de evolução

Como este é um projeto temporário, algumas melhorias futuras podem ser adicionadas conforme a necessidade do processo de mudança:

- Autenticação de usuários para controlar quem pode registrar baixas.
- Histórico completo de movimentações por equipamento.
- Tela de busca e filtros por patrimônio, nome ou status.
- Exportação de relatórios em Excel ou PDF.
- Melhor tratamento de erros na leitura da câmera.
- Confirmação de saída com data, responsável e destino editáveis no momento do registro.
- Painel de acompanhamento com totais, itens restantes e itens já baixados.
- Validação para impedir duplicidade de registros.
- Versão mobile mais otimizada para uso em campo.

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
streamlit run app.py
```

## Observação

O projeto foi pensado para apoiar uma operação específica de mudança de sede, mas a lógica pode ser adaptada para outros cenários de controle patrimonial e logística interna.
