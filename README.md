Loan Eligibility Predictor:

Project Overview
The Loan Eligibility Predictor is a machine learning–based web application that predicts whether a loan should be approved or not based on applicant details. It uses historical data and ML models along with basic rule-based validation to make realistic loan decisions. The application is built using Python, Flask, HTML, CSS, and JavaScript.

Objective
To help banks or fintech platforms quickly assess loan eligibility by analyzing user inputs such as income, credit score, education, and employment status.

Technologies Used
Python
Flask
Pandas
NumPy
Scikit-learn
Matplotlib
HTML, CSS, JavaScript
Joblib

Features
User-friendly web interface
Machine Learning models (Logistic Regression / Random Forest)
Rule-based validation for credit score and income
Real-time loan approval or rejection
Flask backend integration

📁 Project Structure
Loan-Eligibility-Predictor/
│── app/
│   ├── app.py
│   ├── templates/index.html
│   └── static/script.js
│       |_style.css
│── data/
│   └── loan_data.csv
│
│── notebooks/
│   └── loan_model.ipynb
│
│── src/
│   ├── loan_model.pkl
│   └── scaler.pkl
│
│── images/


 How to Run the Project (VS Code)
1️. Clone or Download the Repository
git clone <your-github-link>
cd Loan-Eligibility-Predictor

2️. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

. Install Dependencies
pip install -r requirements.txt

4️. Run Flask App
cd app
python app.py

5.Open browser and go to:
http://127.0.0.1:5000 


📝 Input Fields
Age,
Income,
Education,
Credit Score,
Employment Status,
Loan Amount

📈 Output
Loan Approved
Loan Not Approved
Displays rejection reason if eligibility rules fail
