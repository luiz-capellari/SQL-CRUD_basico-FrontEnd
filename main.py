from data_base import connect_db
import panda as pd

engine = connect_db()

if engine is not None:
    pd.read_excel('equipamentos.xlsx')

    df.to_sql(
        name='equipamentos_estudios',
        con=engine,
        if_exists='append',
        index=False
    )
    print("Planilha de equipamentos importada com sucesso!")

    




