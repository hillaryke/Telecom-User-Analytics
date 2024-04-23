import unittest
import pandas as pd
from src.database_connection import get_data_from_db

class TestDatabaseConnection(unittest.TestCase):
    def test_get_data_from_db(self):
        df = get_data_from_db()

        # Check if the function returns a DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # Check if the DataFrame is not empty
        self.assertFalse(df.empty)


if __name__ == '__main__':
    unittest.main()
