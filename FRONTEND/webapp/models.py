from django.db import models # type: ignore
import numpy as np
import pickle

# Load the trained ML model (replace with the actual model path)
model = pickle.load(open(r'C:\Users\mouni\OneDrive\OfficeMobile\Documents\project\PROJECT\MEDICINE_RECOMMENDATION\DATASET\xgboost.pkl', 'rb'))

# Function to predict disease based on symptoms
def predict_disease(symptom_list):
    """
    Predict the disease based on the given symptoms.

    Args:
        symptom_list (list): A list of symptom values (binary: 1 if present, 0 if not).

    Returns:
        str: Predicted disease name.
    """
    symptoms_array = np.array(symptom_list).reshape(1, -1)  # Reshape for model input
    predicted_disease = model.predict(symptoms_array)[0]  # Get the prediction
    return predicted_disease
