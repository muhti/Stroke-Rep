# -*- coding: utf-8 -*-
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from .model import load_model, predict
import pandas as pd

app = FastAPI()

model = load_model()

class InputData(BaseModel):
    age: float
    hypertension: bool
    heart_disease: bool
    avg_glucose_level: float
    bmi: Optional[float] = None
    ever_married: str
    work_type: str
    smoking_status: str

@app.post("/predict/")
def make_prediction(input_data: InputData):
    input_df = pd.DataFrame([dict(input_data)])
    prediction = predict(model, input_df)
    return {"prediction": prediction.tolist()}