import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import joblib
import os

print("Loading dataset...")
data_path = 'healthcare_dataset.csv'
if not os.path.exists(data_path):
    print(f"Error: {data_path} not found.")
    exit(1)

df = pd.read_csv(data_path)

# Drop rows with missing values (if any)
df = df.dropna()

print("Dataset loaded successfully. Shape:", df.shape)

# Create models directory
os.makedirs('models', exist_ok=True)

# ---------------------------------------------------------------------
# Model 1: Predict Medical Condition (Classification)
# ---------------------------------------------------------------------
print("Training Model 1: Medical Condition Predictor...")
features_1 = ['Age', 'Gender', 'Blood Type', 'Admission Type', 'Test Results']
target_1 = 'Medical Condition'

X_1 = df[features_1]
y_1 = df[target_1]

# Preprocessing
categorical_cols_1 = ['Gender', 'Blood Type', 'Admission Type', 'Test Results']
numerical_cols_1 = ['Age']

preprocessor_1 = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols_1),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols_1)
    ])

# Pipeline
clf_1 = Pipeline(steps=[('preprocessor', preprocessor_1),
                        ('classifier', RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42))])

clf_1.fit(X_1, y_1)
joblib.dump(clf_1, 'models/medical_condition_model.pkl')
print("Model 1 saved to models/medical_condition_model.pkl")


# ---------------------------------------------------------------------
# Model 2: Predict Billing Amount (Regression)
# ---------------------------------------------------------------------
print("Training Model 2: Billing Amount Predictor...")
features_2 = ['Age', 'Gender', 'Medical Condition', 'Admission Type', 'Medication']
target_2 = 'Billing Amount'

X_2 = df[features_2]
y_2 = df[target_2]

categorical_cols_2 = ['Gender', 'Medical Condition', 'Admission Type', 'Medication']
numerical_cols_2 = ['Age']

preprocessor_2 = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols_2),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols_2)
    ])

reg_2 = Pipeline(steps=[('preprocessor', preprocessor_2),
                        ('regressor', RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42))])

reg_2.fit(X_2, y_2)
joblib.dump(reg_2, 'models/billing_amount_model.pkl')
print("Model 2 saved to models/billing_amount_model.pkl")


# ---------------------------------------------------------------------
# Model 3: Predict Test Results (Classification)
# ---------------------------------------------------------------------
print("Training Model 3: Test Results Predictor...")
features_3 = ['Age', 'Gender', 'Medical Condition', 'Blood Type', 'Admission Type']
target_3 = 'Test Results'

X_3 = df[features_3]
y_3 = df[target_3]

categorical_cols_3 = ['Gender', 'Medical Condition', 'Blood Type', 'Admission Type']
numerical_cols_3 = ['Age']

preprocessor_3 = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols_3),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols_3)
    ])

clf_3 = Pipeline(steps=[('preprocessor', preprocessor_3),
                        ('classifier', RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42))])

clf_3.fit(X_3, y_3)
joblib.dump(clf_3, 'models/test_results_model.pkl')
print("Model 3 saved to models/test_results_model.pkl")

print("All models trained and saved successfully!")
