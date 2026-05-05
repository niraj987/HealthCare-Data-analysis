from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
import os

app = FastAPI(title="Healthcare ML Interactive Dashboard")

# Mount static files
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Models
models_dir = "models"
try:
    model_condition = joblib.load(os.path.join(models_dir, "medical_condition_model.pkl"))
    model_billing = joblib.load(os.path.join(models_dir, "billing_amount_model.pkl"))
    model_test_results = joblib.load(os.path.join(models_dir, "test_results_model.pkl"))
except Exception as e:
    print(f"Warning: Models not loaded. Please ensure train_models.py has been run. {e}")

# Data Models for API
class ConditionInput(BaseModel):
    Age: int
    Gender: str
    Blood_Type: str
    Admission_Type: str
    Test_Results: str

class BillingInput(BaseModel):
    Age: int
    Gender: str
    Medical_Condition: str
    Admission_Type: str
    Medication: str

class TestResultsInput(BaseModel):
    Age: int
    Gender: str
    Medical_Condition: str
    Blood_Type: str
    Admission_Type: str

@app.get("/")
def serve_home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/predict/condition")
def predict_condition(data: ConditionInput):
    df = pd.DataFrame([{
        "Age": data.Age,
        "Gender": data.Gender,
        "Blood Type": data.Blood_Type,
        "Admission Type": data.Admission_Type,
        "Test Results": data.Test_Results
    }])
    prediction = model_condition.predict(df)[0]
    return {"prediction": prediction}

@app.post("/predict/billing")
def predict_billing(data: BillingInput):
    df = pd.DataFrame([{
        "Age": data.Age,
        "Gender": data.Gender,
        "Medical Condition": data.Medical_Condition,
        "Admission Type": data.Admission_Type,
        "Medication": data.Medication
    }])
    prediction = model_billing.predict(df)[0]
    return {"prediction": round(prediction, 2)}

@app.post("/predict/test_results")
def predict_test_results(data: TestResultsInput):
    df = pd.DataFrame([{
        "Age": data.Age,
        "Gender": data.Gender,
        "Medical Condition": data.Medical_Condition,
        "Blood Type": data.Blood_Type,
        "Admission Type": data.Admission_Type
    }])
    prediction = model_test_results.predict(df)[0]
    return {"prediction": prediction}

# Endpoints for EDA Data
@app.get("/api/eda_data")
def get_eda_data():
    # Load dataset for aggregate data
    df = pd.read_csv("healthcare_dataset.csv")
    
    # 1. Condition by Gender
    condition_gender = df.groupby(["Medical Condition", "Gender"]).size().unstack().fillna(0).to_dict()
    
    # 2. Billing by Admission Type
    billing_admission = df.groupby("Admission Type")["Billing Amount"].sum().to_dict()
    
    # 3. Blood type distribution
    blood_type = df["Blood Type"].value_counts().to_dict()
    
    return {
        "condition_gender": condition_gender,
        "billing_admission": billing_admission,
        "blood_type": blood_type
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
