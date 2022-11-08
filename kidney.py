from flask import Flask, render_template, url_for,  flash, redirect
import joblib
import numpy as np
from flask import request
app = Flask(__name__, template_folder='templates')


@app.route("/")

def home():
    return render_template("index.html")

@app.route('/result_true')
def result_true():
    return render_template('result_true.html')

@app.route('/result_false')
def result_false():
    return render_template('result_false.html')


@app.route("/kidney")
def kidney():
    return render_template('kidney.html')

def KidneyPredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==12):
        loaded_model = joblib.load('HealthCareApp\\pickle files\\diabetes.pkl')
        result4 = loaded_model.predict(to_predict)
    return result4[0]

@app.route('/submit4', methods = ["POST"])
def submit4():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==12):
            result4 = KidneyPredictor(to_predict_list,12)
    if(int(result4)==1):
        return result_true()
    else:
        return result_false()
app.run(debug=True)