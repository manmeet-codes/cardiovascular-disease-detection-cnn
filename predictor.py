import numpy as np
import pickle

# Load Logistic Regression model
with open('model/best_lr.pkl', 'rb') as f:
    lr_model = pickle.load(f)


def predict_cvd(data):
    """
    Predict cardiovascular disease risk using clinical parameters
    """

    # Convert input to numpy array
    input_array = np.asarray(data)

    # Reshape for sklearn (1 sample, n features)
    input_array = input_array.reshape(1, -1)

    # Make prediction
    prediction = lr_model.predict(input_array)

    return int(prediction[0])