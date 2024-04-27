from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import pandas as pd

def preprocess_data(df, timestamp_cols, numeric_features, categorical_features):
    # Convert the 'End time of the xDR (last frame timestamp)' and 'Start' columns to datetime
    timestamp_features = []
    for col in timestamp_cols:
        df[col] = pd.to_datetime(df[col])

        # Extract features from the timestamp columns
        df[f'{col}_hour'] = df[col].dt.hour
        df[f'{col}_day_of_week'] = df[col].dt.dayofweek
        df[f'{col}_day_of_month'] = df[col].dt.day
        df[f'{col}_month'] = df[col].dt.month

        # Add the new features to the timestamp_features list
        timestamp_features.extend([f'{col}_hour', f'{col}_day_of_week', f'{col}_day_of_month', f'{col}_month'])

    # Identify numeric columns
    if numeric_features is None:
        numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Remove timestamp features from the numeric_features list
    numeric_features = [feature for feature in numeric_features if feature not in timestamp_features]

    # Define preprocessing for numeric columns (replace missing values with mean and scale values)
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features)])

    # Fit and transform the data
    df_preprocessed = preprocessor.fit_transform(df)

    # Convert the preprocessed data back to a DataFrame
    df_preprocessed = pd.DataFrame(df_preprocessed, columns=numeric_features)

    return df_preprocessed