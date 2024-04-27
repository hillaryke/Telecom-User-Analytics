from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd

def preprocess_data(df, timestamp_cols, numeric_features, categorical_features, numeric_scaling=None):
    # Replace 'undefined' with NaN
    df.replace('undefined', np.nan, inplace=True)

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

    # Remove timestamp features from the numeric_features list
    numeric_features = [feature for feature in numeric_features if feature not in timestamp_features]

    # Remove categorical features from the numeric_features list
    numeric_features = [feature for feature in numeric_features if feature not in categorical_features]

    # Define preprocessing for numeric columns (replace missing values with mean and scale values)
    if numeric_scaling:
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())])
    else:
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean'))])

    # Define preprocessing for categorical columns (replace missing values with mode)
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent'))])

    # Define the preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    # Fit and transform the data
    df_preprocessed = preprocessor.fit_transform(df)

    # Get feature names after transformation
    numeric_features_transformed = preprocessor.transformers_[0][-1]
    categorical_features_transformed = preprocessor.transformers_[1][-1]

    # Convert the preprocessed data back to a DataFrame
    df_preprocessed = pd.DataFrame(df_preprocessed, columns=numeric_features_transformed + categorical_features_transformed)

    return df_preprocessed