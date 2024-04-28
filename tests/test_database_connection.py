import os
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

    def test_export_to_csv(self):
        query = "SELECT * FROM xdr_data"
        file_name = 'test_export.csv'
        self.data_loader.load_data_and_export_to_csv(query, file_name)

        # Check if the file is created
        self.assertTrue(os.path.isfile(file_name))
        # Clean up after test
        os.remove(file_name)

if __name__ == '__main__':
    unittest.main()