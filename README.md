# Stroke Prediction App

## Project Overview

This project utilizes FastAPI to deploy a machine learning model capable of predicting stroke occurrences. The model is trained using health-related input features.

## Features

- Prediction of stroke occurrences using health-related input features such as age, hypertension status, heart disease status, average glucose level, body mass index (BMI), marital status, type of work, and smoking status.
- Efficient request handling using FastAPI framework.
- Integration with a trained machine learning model for accurate stroke prediction.

## Installation

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository

```bash
git clone https://your-repository-url.com
cd stroke_prediction_app
```

### 2. Set Up a Virtual Environment

```bash
# Create a virtual environment (for Windows)
py -m venv venv

# Create a virtual environment (for Unix or MacOS)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # Unix or MacOS
.\venv\Scripts\activate   # Windows
```

### 3.Install Dependencies

```bash
pip install -r requirements.txt
```

### USAGE

```bash
uvicorn app.main:app --reload
```

### License

[MIT](https://choosealicense.com/licenses/mit/)
