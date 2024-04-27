from src.database_handler import DatabaseHandler
from src.config import db_config

# Create an instance of DatabaseHandler at the module level
db_handler = DatabaseHandler(db_config)

def fetch_data_from_db(query):
    df = db_handler.get_data_from_db(query)
    return df

def save_data_to_db(df, table_name):
    db_handler.store_data_in_db(df, table_name)

def fetch_telecom_data():
    return fetch_data_from_db_table('xdr_data')

def fetch_data_from_db_table(table_name):
    query = f'SELECT * FROM {table_name}'
    return fetch_data_from_db(query)