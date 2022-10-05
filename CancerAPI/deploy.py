
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

#load model
model = pickle.load(open('C:\\Users\\divya\\OneDrive\\Desktop\\HealthCareApp\\HealthCareApp\\CancerAPI\\cancer.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('C:\\Users\\divya\\OneDrive\\Desktop\\HealthCareApp\\HealthCareApp\\CancerAPI\\templates\\index.html', **locals())

@app.route('/submit', methods=['POST', 'GET'])
def predict():
    if request.method==['POST']:
        Concave_Points_Mean = request['Concave Points Mean']
        Area_Mean = request.form['Area Mean']
        Radius_Mean = request.form['Radius Mean']
        Perimeter_Mean = request.form['Perimeter Mean']
        Concavity_Mean = request.form['Concavity Mean']

    result = model.predict([[ Concave_Points_Mean,Area_Mean,  Radius_Mean, Perimeter_Mean, Concavity_Mean]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug= True)