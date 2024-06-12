import pickle
from pathlib import Path

def load_model():
    model_path = Path(__file__).parent / "../models/trained_pipeline-0.1.0.pkl"
    with model_path.open("rb") as model_file:
        model = pickle.load(model_file)
    return model

def predict(model, input_data):
    return model.predict(input_data)