import unittest
import pandas as pd
from src.loader import DataLoader

class TestDatabaseConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_loader = DataLoader()

    def test_load_data(self):
        query = "SELECT * FROM xdr_data"
        df = self.data_loader.load_data(query)

        # Check if the function returns a DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # Check if the DataFrame is not empty
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()