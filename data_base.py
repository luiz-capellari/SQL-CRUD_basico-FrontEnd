import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def connect_db():
    
    try:
    
            dbname = os.getenv("DB_NAME")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")
            host = os.getenv("DB_HOST")
            port = os.getenv("DB_PORT")
        
            db_url = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
    
            engine = create_engine(db_url)

            print('Conexão com o Banco de Dados feita com sucesso!')

            return engine

    except OSError as e:
            print(f'Houve uma falha ao conectar ao Banco de Dados (Postgres): {e}')

            return None

