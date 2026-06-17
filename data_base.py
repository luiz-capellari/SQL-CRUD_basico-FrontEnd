import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    
    try:
        conn = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT")
        )
        print('Banco de dados conectado!')
        return conn
    except Error as e:
        print(f'Houve uma falha ao conectar ao Banco de Dados (Postgres): {e}')
        

connection = connect_db()

# PARA EU TESTAR A CONEXÃO COM O BANCO DE DADOS
# if connection is not None:
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM usarios')
#     usuarios = cursor.fetchall()

#     print(usuarios)
   
def desconect():
    cursor = connection.cursor()
    if cursor:
        cursor.close()
        connection.close()
    return (f'("Banco de dados desconectado!")')

