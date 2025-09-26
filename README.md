 Student Score Prediction

A machine learning project that predicts **student GPA** based on study time, parental support, absences, and class grade.  
This project uses **Linear Regression** and **Polynomial Regression** models and is deployed with **Flask**.

---
Features
- Predicts GPA from student data  using python
- Web interface using Flask + HTML  
- Linear & Polynomial Regression comparison  
- Jupyter Notebook included for analysis  

Student-Score-Prediction/
│── index.html -Frontend (form for input & output)
│── app.py - Flask backend
│── score.ipynb - Jupyter Notebook (model training & testing)
│── dataset.csv -Dataset used
│── requirements.txt -Dependencies
│── README.md -Project documentation

1. Installation & Setup
 Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/student-score-prediction.git
   cd student-score-prediction
2. Install dependencies:
pip install -r requirements.txt

3. Run Flask app:
python app.py

4. Open in browser:
http://127.0.0.1:5000/
