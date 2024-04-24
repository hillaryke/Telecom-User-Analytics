import unittest
import pandas as pd
from src.database_connection import DatabaseHandler
from src.config import db_config
from sqlalchemy import text

class TestDatabaseHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_handler = DatabaseHandler(db_config)

    def test_get_data_from_db(self):
        query = "SELECT * FROM xdr_data"
        df = self.db_handler.get_data_from_db(query)

        # Check if the function returns a DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # Check if the DataFrame is not empty
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()