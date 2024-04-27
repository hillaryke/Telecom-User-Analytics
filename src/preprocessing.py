from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from scipy.stats import skew
import pandas as pd
import numpy as np

def replace_undefined_with_nan(df):
    df.replace('undefined', np.nan, inplace=True)
    return df

def handle_outliers_mode(df, numeric_features):
    for feature in numeric_features:
        mode = df[feature].mode()[0]
        Q1 = df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df[feature] = np.where((df[feature] < lower_bound) | (df[feature] > upper_bound), mode, df[feature])
    return df

def handle_outliers_log(df, numeric_features):
    for feature in numeric_features:
        # Apply log transformation to each feature
        df[feature] = np.log1p(df[feature])
    return df

def handle_outliers_mean_mode(df, numeric_features):
    df = handle_outliers_log(df, numeric_features)
    for feature in numeric_features:
        if skew(df[feature]) > 0.5:  # if the data is skewed, use the median
            median = df[feature].median()
            Q1 = df[feature].quantile(0.25)
            Q3 = df[feature].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            df[feature] = np.where((df[feature] < lower_bound) | (df[feature] > upper_bound), median, df[feature])
        else:  # if the data is not skewed, use the mean
            mean = df[feature].mean()
            std = df[feature].std()

            lower_bound = mean - 2 * std
            upper_bound = mean + 2 * std

            df[feature] = np.where((df[feature] < lower_bound) | (df[feature] > upper_bound), mean, df[feature])
    return df

def handle_outliers_median(df, numeric_features):
    df = handle_outliers_log(df, numeric_features)
    for feature in numeric_features:
        median = df[feature].median()
        Q1 = df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df[feature] = np.where((df[feature] < lower_bound) | (df[feature] > upper_bound), median, df[feature])
    return df

def convert_to_datetime(df, timestamp_cols, numeric_features, categorical_features):
    timestamp_features = []
    for col in timestamp_cols:
        df[col] = pd.to_datetime(df[col])
        df[f'{col}_hour'] = df[col].dt.hour
        df[f'{col}_day_of_week'] = df[col].dt.dayofweek
        df[f'{col}_day_of_month'] = df[col].dt.day
        df[f'{col}_month'] = df[col].dt.month
        timestamp_features.extend([f'{col}_hour', f'{col}_day_of_week', f'{col}_day_of_month', f'{col}_month'])
    numeric_features = [feature for feature in numeric_features if feature not in timestamp_features]
    return df, numeric_features, categorical_features

def preprocess_numeric(df, numeric_features, numeric_scaling=None):
    if numeric_scaling:
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())])
    else:
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean'))])
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features)])
    df_preprocessed = preprocessor.fit_transform(df)
    numeric_features_transformed = preprocessor.transformers_[0][-1]
    df_preprocessed = pd.DataFrame(df_preprocessed, columns=numeric_features_transformed)
    return df_preprocessed

def preprocess_categorical(df, categorical_features):
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent'))])
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_features)])
    df_preprocessed = preprocessor.fit_transform(df)
    categorical_features_transformed = preprocessor.transformers_[0][-1]
    df_preprocessed = pd.DataFrame(df_preprocessed, columns=categorical_features_transformed)
    return df_preprocessed

def preprocess_data(df, categorical_features, numerical_features, numeric_scaling=None, timestamp_cols=None):
    # remove duplicate features
    for feature in categorical_features:
        if feature in numerical_features:
            numerical_features.remove(feature)

    # Check for duplicate features
    duplicate_features = set(categorical_features) & set(numerical_features)
    if duplicate_features:
        raise ValueError(f"Duplicate features in numeric and categorical features: {duplicate_features}")


    df = replace_undefined_with_nan(df)
    df = handle_outliers_median(df, numerical_features)
    df_numeric = preprocess_numeric(df, numerical_features, numeric_scaling)
    df_categorical = preprocess_categorical(df, categorical_features)

    # Combine the numeric and categorical dataframes
    df_preprocessed = pd.merge(df_numeric, df_categorical, left_index=True, right_index=True)

    return df_preprocessed