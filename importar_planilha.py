from data_base import connect_db
import pandas as pd
import openpyxl

engine = connect_db()

if engine is not None:
    df = pd.read_excel('equipamentos.xlsx')
    # metodo para evocar planilha com pandas para sql
    df.to_sql(
        name='equipamentos_estudios',
        con=engine,
        if_exists='append',
        index=False
    )
    print("Planilha de equipamentos importada com sucesso!")






