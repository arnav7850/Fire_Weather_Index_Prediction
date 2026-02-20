📌 Project Overview

This project is a Machine Learning Web Application that predicts the Fire Weather Index (FWI) using a trained Ridge Regression model.

The application is built using:

Python

Flask

Scikit-learn

Pandas

HTML

Users can input environmental parameters, and the system predicts the Fire Weather Index value.

🚀 Features

Clean Home Page

Separate Prediction Page

Ridge Regression Model

StandardScaler preprocessing

Real-time prediction using Flask

Simple and clean UI


🧠 Machine Learning Model

Model: Ridge Regression

Preprocessing: StandardScaler

Model and scaler saved using pickle

Trained on Fire Weather dataset



FWI/
│
├── application.py
├── README.md
├── Models/
│   ├── model_1.pkl
│   └── scaler_1.pkl
│
├── templates/
│   ├── home.html
│   └── index.html
│
└── requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <your-repository-link>
cd FWI

2️⃣ Create Virtual Environment
python -m venv .venv


Activate the environment:

Windows

.venv\Scripts\activate


Mac/Linux

source .venv/bin/activate

3️⃣ Install Dependencies
python -m pip install -r requirements.txt

4️⃣ Run the Application
python application.py


Open your browser and go to:

http://127.0.0.1:5000/

📊 Input Features

The model requires the following inputs:

Temperature

RH (Relative Humidity)

Ws (Wind Speed)

Rain

FFMC

DMC

ISI

Classes

Region

🔄 Application Flow

User visits the Home Page

Clicks on "Go to Prediction Page"

Enters environmental parameters

Data is scaled using StandardScaler

Ridge Regression model predicts FWI

Result is displayed on the prediction page

🎯 Future Improvements

Improve UI using Bootstrap

Add input validation

Add error handling

Deploy on Render / Railway / AWS

Dockerize the project

👨‍💻 Author

Arnav Raj
CSE (AIML) Student
Machine Learning & Web Development Enthusiast

📜 License

This project is for educational and portfolio purposes.