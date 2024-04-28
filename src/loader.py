from src.utils import fetch_data_from_db, export_to_csv

class DataLoader:
    def __init__(self):
        pass

    def load_data(self, query: str):
        df = fetch_data_from_db(query)
        return df

    def load_data_and_export_to_csv(self, query: str, file_name: str):
        df = self.load_data(query)
        export_to_csv(df, file_name)