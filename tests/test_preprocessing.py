import unittest
import pandas as pd
import numpy as np
from src.preprocessing import preprocess_numeric, preprocess_categorical

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'numeric': [1, 2, 3, np.nan, 5],
            'categorical': ['cat', 'dog', 'cat', 'dog', np.nan],
        })
        self.numeric_features = ['numeric']
        self.categorical_features = ['categorical']

    def test_gh_preprocess_numeric(self):
        df_numeric = preprocess_numeric(self.data, self.numeric_features)

        # Check if the function returns a DataFrame
        self.assertIsInstance(df_numeric, pd.DataFrame)

        # Check if the DataFrame is not empty
        self.assertFalse(df_numeric.empty)

        # Check if the DataFrame has the correct number of columns
        self.assertEqual(len(df_numeric.columns), 1)

        # Check if the DataFrame has the correct columns
        expected_columns = ['numeric']
        self.assertListEqual(list(df_numeric.columns), expected_columns)

    def test_gh_preprocess_categorical(self):
        df_categorical = preprocess_categorical(self.data, self.categorical_features)

        # Check if the function returns a DataFrame
        self.assertIsInstance(df_categorical, pd.DataFrame)

        # Check if the DataFrame is not empty
        self.assertFalse(df_categorical.empty)

        # Check if the DataFrame has the correct number of columns
        self.assertEqual(len(df_categorical.columns), 1)

        # Check if the DataFrame has the correct columns
        expected_columns = ['categorical']
        self.assertListEqual(list(df_categorical.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()