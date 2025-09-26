from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

# =======================
# 1. Flask App
# =======================
app = Flask(__name__)

# =======================
# 2. Load Trained Models
# =======================
lin_model = joblib.load("linear_model.pkl")
poly_model = joblib.load("poly_model.pkl")
poly_transform = joblib.load("poly_transform.pkl")  # PolynomialFeatures object

# =======================
# 3. Home Route
# =======================
@app.route('/')
def home():
    return render_template("score_index.html", lin_result=None, poly_result=None)

# =======================
# 4. Prediction Route
# =======================
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    
    # Convert all inputs to float
    input_values = [float(value) for value in data.values()]
    input_array = np.array(input_values).reshape(1, -1)

    # Predictions
    lin_pred = lin_model.predict(input_array)[0]
    poly_pred = poly_model.predict(poly_transform.transform(input_array))[0]

    return render_template(
        "score_index.html",
        lin_result = round(lin_pred, 2),
        poly_result = round(poly_pred, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
