from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, df, timestamp_cols, numeric_features, categorical_features, numeric_scaling=None):
        self.df = df
        self.timestamp_cols = timestamp_cols
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features
        self.numeric_scaling = numeric_scaling

    def replace_undefined_with_nan(self):
        self.df.replace('undefined', np.nan, inplace=True)
        return self.df

    def handle_outliers(self):
        self.df = handle_outliers_mean_mode(self.df, self.numeric_features)
        return self.df

    def convert_to_datetime(self):
        timestamp_features = []
        for col in self.timestamp_cols:
            self.df[col] = pd.to_datetime(self.df[col])
            self.df[f'{col}_hour'] = self.df[col].dt.hour
            self.df[f'{col}_day_of_week'] = self.df[col].dt.dayofweek
            self.df[f'{col}_day_of_month'] = self.df[col].dt.day
            self.df[f'{col}_month'] = self.df[col].dt.month
            timestamp_features.extend([f'{col}_hour', f'{col}_day_of_week', f'{col}_day_of_month', f'{col}_month'])
        self.numeric_features = [feature for feature in self.numeric_features if feature not in timestamp_features]
        self.numeric_features = [feature for feature in self.numeric_features if feature not in self.categorical_features]
        return self.df

    def preprocess_numeric_and_categorical(self):
        if self.numeric_scaling:
            numeric_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())])
        else:
            numeric_transformer = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median'))])
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent'))])
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, self.numeric_features),
                ('cat', categorical_transformer, self.categorical_features)])
        df_preprocessed = preprocessor.fit_transform(self.df)
        numeric_features_transformed = preprocessor.transformers_[0][-1]
        categorical_features_transformed = preprocessor.transformers_[1][-1]
        df_preprocessed = pd.DataFrame(df_preprocessed, columns=numeric_features_transformed + categorical_features_transformed)
        return df_preprocessed

    def preprocess_data(self):
        self.replace_undefined_with_nan()
        self.handle_outliers()
        self.convert_to_datetime()
        df_preprocessed = self.preprocess_numeric_and_categorical()
        return df_preprocessed