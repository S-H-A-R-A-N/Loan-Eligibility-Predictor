from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler
model = joblib.load(os.path.join("..", "src", "loan_model.pkl"))
scaler = joblib.load(os.path.join("..", "src", "scaler.pkl"))

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = float(request.form['age'])
        income = float(request.form['income'])
        education = int(request.form['education'])
        credit_score = float(request.form['credit_score'])
        employment_status = int(request.form['employment_status'])
        loan_amount = float(request.form['loan_amount'])

        # 🚨 Manual safety rules (IMPORTANT)
        if credit_score < 600:
            result = "Not Approved (Low Credit Score)"
            return render_template('index.html', result=result)

        if income < 20000:
            result = "Not Approved (Low Income)"
            return render_template('index.html', result=result)

        # Create array and scale features
        X = np.array([[age, income, credit_score, loan_amount, education, employment_status]])
        X_scaled = scaler.transform(X)

        # ML prediction
        pred = model.predict(X_scaled)[0]

        result = "Approved" if pred == 1 else "Not Approved"
        return render_template('index.html', result=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
