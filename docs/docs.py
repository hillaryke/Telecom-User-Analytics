from src.utils import fetch_data_from_db


class DataLoader:
    """
    DataLoader class is responsible for loading data from a database.

    Methods:
        load_data(query: str) -> pd.DataFrame:
            Load data from a database based on a provided SQL query.
    """

    def __init__(self):
        pass

    def load_data(self, query: str):
        """
        Load data from a database based on a provided SQL query.

        Parameters:
            query (str): The SQL query to fetch data.

        Returns:
            df (pd.DataFrame): The loaded data.
        """
        df = fetch_data_from_db(query)
        return df