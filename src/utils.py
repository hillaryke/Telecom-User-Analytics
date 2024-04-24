from sqlalchemy import text
from src.database_connection import DatabaseHandler
from src.config import db_config

def fetch_data_from_db(query):
    db_handler = DatabaseHandler(db_config)
    df = db_handler.get_data_from_db(query)
    return df
