from src.utils import fetch_data_from_db

class DataLoader:
    def __init__(self):
        pass

    def load_data(self, query: str):
        df = fetch_data_from_db(query)
        return df