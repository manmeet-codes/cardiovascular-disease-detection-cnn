from flask import Flask, render_template, request
import numpy as np
from PIL import Image
import joblib
import tensorflow as tf

app = Flask(__name__)

# Load models
cnn_model = tf.keras.models.load_model('model/cnn_model.h5')
lr_model = joblib.load('model/best_lr.pkl')

# Class labels
classes = ["abnormal", "history_mi", "mi", "normal"]


@app.route('/', methods=['GET', 'POST'])
def index():
    cnn_prediction = None
    confidences = None
    lr_prediction = None

    if request.method == 'POST':

        # ECG Image Prediction
        if 'image' in request.files:
            file = request.files['image']

            if file and file.filename != '':
                img = Image.open(file).convert('RGB')
                img = img.resize((256, 128))

                img_array = np.array(img) / 255.0
                img_array = np.expand_dims(img_array, axis=0)

                prediction = cnn_model.predict(img_array)[0]
                predicted_class = np.argmax(prediction)

                cnn_prediction = classes[predicted_class].replace("_", " ").title()

                confidences = {
                    classes[i].replace("_"," ").title(): round(float(prediction[i]) * 100, 2)
                    for i in range(len(classes))
                }

        # Clinical Data Prediction
        elif all(k in request.form for k in [
            'age','height','weight','gender','ap_hi','ap_lo',
            'cholesterol','gluc','smoke','alco','active'
        ]):

            try:
                user_input = [
                    float(request.form.get('age')),
                    float(request.form.get('height')),
                    float(request.form.get('weight')),
                    float(request.form.get('gender')),
                    float(request.form.get('ap_hi')),
                    float(request.form.get('ap_lo')),
                    float(request.form.get('cholesterol')),
                    float(request.form.get('gluc')),
                    float(request.form.get('smoke')),
                    float(request.form.get('alco')),
                    float(request.form.get('active'))
                ]

                prediction = lr_model.predict([user_input])[0]

                lr_prediction = "Cardiovascular Disease Risk" if prediction == 1 else "Healthy"

            except Exception as e:
                lr_prediction = f"Error: {str(e)}"

    return render_template(
        'index.html',
        cnn_prediction=cnn_prediction,
        confidences=confidences,
        classes=classes,
        lr_prediction=lr_prediction
    )


if __name__ == '__main__':
    app.run(debug=True)