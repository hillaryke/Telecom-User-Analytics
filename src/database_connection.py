from utils import export_to_csv

class DatabaseHandler:
    def __init__(self, db_config):
        self.db_config = db_config
        self.engine = create_engine(f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

    def get_data_from_db(self, query: str, export_csv: bool = False, file_name: str = ''):
        query = text(query)
        with self.engine.connect() as conn:
            df = pd.read_sql_query(query, conn)

        if export_csv:
            export_to_csv(df, file_name)

        return df