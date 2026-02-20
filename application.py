import pickle
from flask import Flask,render_template,request,jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app=application

# import ridge regession model and standard scaler
print("Starting app...")

ridge_model = pickle.load(open("Models/model_1.pkl","rb"))
print("Model loaded successfully")

standard_scaler = pickle.load(open("Models/scaler_1.pkl","rb"))
print("Scaler loaded successfully")

    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "POST":
        
        ## read all input values from the form
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))

        ## data preprocessing and feature engineering
        data = pd.DataFrame(
        [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]],
        columns=["Temperature","RH","Ws","Rain","FFMC","DMC","ISI","Classes","Region"]
        )
        new_data_scaled = standard_scaler.transform(data)

        ## predict the FWI value using the ridge regression model
        result = ridge_model.predict(new_data_scaled)

        ##         return the predicted FWI value to the user
        return render_template("index.html",results=result[0])
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)