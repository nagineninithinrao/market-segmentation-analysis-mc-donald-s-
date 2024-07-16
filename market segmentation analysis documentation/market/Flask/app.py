from flask import Flask,render_template,url_for,request
from flask import request,jsonify
import numpy as np
import pandas as pd
import pickle
import joblib
from sklearn.preprocessing import StandardScaler

model=joblib.load(open('model.pkl','rb'))
scaler=joblib.load(open('scaler3.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/output', methods=['GET', 'POST'])
def predict():
    yummy =int(request.form['yummy'])
    convenient=int(request.form['convenient'])
    spicy=int(request.form['spicy']) 
    fattening=int(request.form['fattening'])
    greasy=int(request.form['greasy']) 
    fast=int(request.form['fast'])
    cheap =int(request.form['cheap'])
    tasty =int(request.form['tasty'])
    expensive =int(request.form['expensive'])
    healthy =int(request.form['healthy'])
    disgusting=int(request.form['disgusting'])
    Age=int(request.form['Age'])
    Gender=int(request.form['Gender'])
    total=[[yummy, convenient, spicy, fattening, greasy, fast, cheap,
            tasty, expensive, healthy, disgusting, Age, Gender]]
    prediction=model.predict(scaler.transform(total))
    prediction =int(prediction[0])
    if prediction==0:
        return render_template('output.html',predict="Predicts Customer belong to cluster 0")
    if prediction==1:
        return render_template('output.html',predict="Predicts Customer belong to cluster 1")
    if prediction==2:
        return render_template('output.html',predict="Predicts Customer belong to cluster 2")
    else:
        return render_template('output.html',predict="Predicts Customer belong to cluster 3")
if __name__ == "__main__":
    app.run(debug=True)