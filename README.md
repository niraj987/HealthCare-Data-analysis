# HealthCare-Data-analysis & Machine Learning Integration

An interactive and innovative repository for analyzing healthcare data and applying Machine Learning to predict patient outcomes and hospital billing.

## 🚀 New Features

We have transformed the static data analysis into a **Premium Interactive Dashboard** powered by FastAPI and modern UI principles (Glassmorphism). 

Additionally, we integrated **3 Machine Learning Problem Statements**:
1. **Medical Condition Prediction (Classification)**: Predicts a patient's condition based on demographics, blood type, and test results using a Random Forest Classifier.
2. **Billing Amount Estimator (Regression)**: Forecasts hospital billing costs based on the patient's age, condition, admission type, and medication using a Random Forest Regressor.
3. **Test Results Predictor (Classification)**: Predicts whether upcoming tests will be Normal, Abnormal, or Inconclusive.

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, Uvicorn
- **Machine Learning**: Scikit-Learn, Pandas, Numpy, Joblib
- **Frontend**: HTML5, Vanilla CSS (Glassmorphism), Vanilla JS
- **Visualizations**: Chart.js

## 🏃‍♂️ How to Run Locally

1. **Install Dependencies**
   ```bash
   pip install pandas scikit-learn joblib fastapi uvicorn
   ```

2. **Train the Machine Learning Models**
   Generate the `.pkl` model files by running:
   ```bash
   python train_models.py
   ```

3. **Start the Interactive Dashboard**
   Launch the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. **View the Dashboard**
   Open your browser and navigate to: `http://127.0.0.1:8000`

## 📊 Original Data Analysis
The original Exploratory Data Analysis (EDA) is available in the ` HealthCare_Dataset.ipynb` Jupyter Notebook, covering insights such as medical condition distribution by gender, billing amounts across insurance providers, and seasonal temporal patterns of hospital expenditure.
