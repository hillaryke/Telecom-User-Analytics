import pandas as pd
from sqlalchemy import create_engine, text
from src.config import db_config

def get_data_from_db():
    # Create a connection to the PostgreSQL database
    engine = create_engine(f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

    # Execute a SQL query and load the result into a DataFrame
    query = text("SELECT * FROM xdr_data")
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn)

    return df