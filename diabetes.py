from this import d
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

@app.route("/diabetes")
def diabetes():
    return render_template('diabetes.html')

def DiabetesPredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==6):
        loaded_model = joblib.load('HealthCareApp\\pickle files\\diabetes.pkl')
        result3 = loaded_model.predict(to_predict)
    return result3[0]

@app.route('/submit2', methods = ["POST"])
def submit2():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==6):
            result3 = DiabetesPredictor(to_predict_list,6)
    if(int(result3)==1):
        return result_true()
    else:
        return result_false()

app.run(debug=True)