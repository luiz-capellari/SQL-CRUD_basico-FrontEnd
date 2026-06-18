import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def connect_db():
    
    try:
    
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT")
        
            db_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    
            engine = create_engine(db_url)

            print('Conexão com o Banco de Dados feita com sucesso!')

            return engine

    except Error as e:
            print(f'Houve uma falha ao conectar ao Banco de Dados (Postgres): {e}')

            return None

