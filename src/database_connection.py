import pandas as pd
from sqlalchemy import create_engine, text

class DatabaseHandler:
    def __init__(self, db_config):
        self.db_config = db_config
        self.engine = create_engine(f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

    def get_data_from_db(self, query):
        query = text(query)
        with self.engine.connect() as conn:
            df = pd.read_sql_query(query, conn)
        return df