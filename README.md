# Cardiovascular Disease Detection System

A machine learning-based system that predicts cardiovascular disease risk using either **clinical health parameters** or **ECG image analysis**.
This project combines a **Logistic Regression model** for structured clinical data and a **Convolutional Neural Network (CNN)** for ECG image classification.
The models are integrated into a **Flask web application** that allows users to interact with both prediction systems through a simple interface.

This project was developed as part of the **Final Year Project for the B.Tech in Computer Science & Engineering** program at **Gauhati University Institute of Science and Technology**, in collaboration with [Sayan Upadhyay]([https://example.com](https://github.com/saiyan66))

---

## Project Overview

The system provides **two independent prediction methods**:

### 1. Clinical Data Prediction

Uses patient health parameters such as age, blood pressure, cholesterol levels, and lifestyle factors to predict cardiovascular disease risk.

Dataset used: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/data

### 2. ECG Image Prediction

Uses a Convolutional Neural Network (CNN) to classify ECG reports into different cardiac conditions based on waveform patterns.

Users can either **upload an ECG image** or **enter clinical health parameters** to obtain predictions.

Dataset used: https://www.kaggle.com/datasets/evilspirit05/ecg-analysis

---

## Models Used

### Logistic Regression Model (Clinical Data)

Predicts the **risk of cardiovascular disease** using structured health data.

**Input Features**

* age
* gender
* height
* weight
* ap_hi (systolic blood pressure)
* ap_lo (diastolic blood pressure)
* cholesterol
* gluc
* smoke
* alco
* active

**Model Performance**

| Metric                     | Score |
| -------------------------- | ----- |
| Accuracy                   | ~72%  |
| Precision (Positive Class) | 75%   |
| Recall (Positive Class)    | 68%   |
| F1 Score                   | 0.71  |
| ROC-AUC                    | 0.78  |

---

### CNN Model (ECG Image Classification)

Classifies ECG images into **four heart conditions**:

* abnormal
* history_mi
* mi
* normal

**Model Performance**

| Class      | Precision | Recall | F1 Score |
| ---------- | --------- | ------ | -------- |
| abnormal   | 1.00      | 0.89   | 0.94     |
| history_mi | 0.89      | 1.00   | 0.94     |
| mi         | 1.00      | 1.00   | 1.00     |
| normal     | 0.98      | 1.00   | 0.99     |

**Overall Accuracy:** 97%

---

## Tech Stack

* Python
* TensorFlow / Keras
* Scikit-learn
* Flask
* NumPy
* Pandas
* OpenCV
* HTML / CSS

---

## Project Structure

```
cvd-detector/
│
├── app.py
├── model/
│   ├── cnn_model.h5
│   └── best_lr.pkl
│
├── templates/
│   └── index.html
│
├── notebooks/
│   ├── cnn_training.ipynb
│   └── lr_training.ipynb
│
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/cvd-detector.git
cd cvd-detector
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```
python app.py
```

Open the application in your browser:

```
http://127.0.0.1:5000
```

---

## How the System Works

### Clinical Data Prediction

1. User enters health parameters.
2. Data is passed to the Logistic Regression model.
3. The model predicts whether the patient is **at risk of cardiovascular disease**.

### ECG Image Prediction

1. User uploads an ECG image.
2. Image is resized and normalized.
3. The CNN analyzes the waveform pattern.
4. The model predicts the heart condition and displays confidence scores.

---

## Future Improvements

* Train on larger ECG datasets
* Improve model generalization
* Add explainable AI techniques for model interpretation
* Deploy the application to a cloud platform
