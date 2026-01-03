# AI-Driven Disease Prediction and Medicine Recommendation System

This project is a Machine Learning–based web application that predicts diseases based on user-selected symptoms and provides medicine, precautions, diet, and workout recommendations.
The system uses trained ML models integrated with a Django web framework and is deployed as a cloud-based application.

---

## 🚀 Features

- Disease prediction based on symptoms
- Medicine recommendations
- Precaution suggestions
- Diet and workout guidance
- User-friendly web interface
- Cloud deployment (Render)

  ---

## 🧠 Technologies Used

### Machine Learning
- XGBoost
- Scikit-learn
- Pandas
- NumPy

### Web Technologies
- Django (Backend)
- HTML, CSS, JavaScript (Frontend)
- Gunicorn (Production server)

### Deployment
- GitHub
- Render Cloud Platform

---

## 📂 Project Structure
Project/

│

├── BACKEND/

│ └── Drug_Recommendation.ipynb           # Model training notebook

│
├── DATASET/

│ ├── Training.csv

│ ├── description.csv

│ ├── medications.csv

│ ├── precautions_df.csv

│ ├── diets.csv

│ └── workout_df.csv

│

├── FRONTEND/

│ ├── manage.py

│ ├── requirements.txt

│ ├── Procfile

│ ├── db.sqlite3

│ │

│ ├── self/                               # Django project settings

│ │ ├── settings.py

│ │ ├── urls.py

│ │ └── wsgi.py

│ │

│ ├── webapp/                             # Django app

│ │ ├── views.py

│ │ ├── urls.py

│ │ └── models.py

│ │

│ ├── templates/

│ │ ├── index.html

│ │ ├── input.html

│ │ └── output.html

│ │

│ ├── static/

│ └── staticfiles/

│

└── README.md
---
## ⚙️ Setup Instructions (From Scratch)

### 1️⃣ Prerequisites

- Python 3.11+
- Git
- Internet connection

---

### 2️⃣ Clone the Repository

- git clone [https://github.com/Priya-Harshitha/disease-prediction-ml.git](https://github.com/Priya-Harshitha/disease-prediction-ml.git)
- cd disease-prediction-ml

---

### 3️⃣ Create Virtual Environment

- cd FRONTEND
- python -m venv venv
- Activate:

Windows: 

venv\Scripts\activate

Linux / Mac: 

source venv/bin/activate

### 4️⃣ Install Dependencies
- pip install -r requirements.txt

### 5️⃣ Collect Static Files
- python manage.py collectstatic

### 6️⃣ Run the Application Locally
- python manage.py runserver


- Open browser:

http://127.0.0.1:8000

### 🌐 Live Deployment

The project is deployed on Render:

🔗 Live URL:
https://disease-prediction-ml-guky.onrender.com
