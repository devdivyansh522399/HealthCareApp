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



@app.route("/cancer")
def cancer():
    return render_template('cancer.html') 

def CancerPredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        loaded_model = joblib.load('HealthCareApp\\pickle files\\cancer.pkl')
        result1 = loaded_model.predict(to_predict)
    return result1[0]

@app.route('/submit1', methods = ["POST"])
def submit1():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==5):
            result1 = CancerPredictor(to_predict_list,5)
    if(int(result1)==1):
        return result_true()
    else:
        return result_false()



@app.route("/liver")
def liver():
    return render_template('liver.html')

def LiverPredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==10):
        loaded_model = joblib.load('HealthCareApp\\pickle files\\diabetes.pkl')
        result2 = loaded_model.predict(to_predict)
    return result2[0]

@app.route('/submit5', methods = ["POST"])
def submit5():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==10):
            result2 = LiverPredictor(to_predict_list,10)
    if(int(result2)==1):
        return result_true()
    else:
        return result_false()




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


@app.route("/heart")
def heart():
    return render_template('heart.html')

def HeartPredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        loaded_model = joblib.load('HealthCareApp\\pickle files\\diabetes.pkl')
        result5 = loaded_model.predict(to_predict)
    return result5[0]

@app.route('/submit3', methods = ["POST"])
def submit3():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        print(len(to_predict_list)==7)
        result5 = HeartPredictor(to_predict_list,7)
    if(int(result5)==1):
        return result_true()
    else:
        return result_false()

app.run(debug=True)