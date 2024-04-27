import unittest
from src.preprocessing import preprocess_data
from src.utils import fetch_telecom_data

class TestPreprocessData(unittest.TestCase):
    def test_unique_columns(self):
        # Load the data
        df = fetch_telecom_data()

        # Define the columns
        timestamp_cols = ['Start', 'End']
        numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_features = ['IMSI', 'MSISDN/Number', 'IMEI', 'Last Location Name', 'Handset Type', 'Handset Manufacturer']

        # Preprocess the data
        df_preprocessed = preprocess_data(df, timestamp_cols, numeric_features, categorical_features)

        # Check if the columns of the returned DataFrame are unique
        self.assertTrue(df_preprocessed.columns.is_unique, "The columns in the preprocessed DataFrame are not unique.")

if __name__ == '__main__':
    unittest.main()