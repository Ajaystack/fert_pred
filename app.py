﻿from flask import Flask,request, url_for, redirect, render_template, request, jsonify
import pickle 
import numpy as np 

app = Flask(__name__)
pkl_filename='pickle_model.pkl'
model=pickle.load(open(pkl_filename ,'rb'))

ctdict = {1:'Barley', 2:'Cotton', 3:'Groundnuts', 4:'Maize', 5:'Millets', 6:'Oil Seeds', 7:'Paddy', 8:'Pulses', 9:'Sugarcane', 10:'Tobacco', 11:'Wheat'}
stdict = {1:'Black', 2:'Clayey', 3:'Loamy', 4:'Red', 5:'Sandy'}
ferdict = {1:'DAP', 2:'14-35-14', 3:'17-17-17', 4:'10-26-26', 5:'28-28', 6:'20-20', 7:'Urea'}

@app.route('/', methods=['POST','GET']) 
def blank(): 
    return redirect(url_for('predict'))
    
@app.route('/ML/about/', methods=['POST','GET']) 
def about(): 
    return render_template('about.html')
    
@app.route('/ML/team/', methods=['POST','GET']) 
def team(): 
    return render_template('team.html')
    
@app.route('/blogs/', methods=['POST','GET']) 
def blog(): 
    return render_template('blog.html')
    
@app.route('/predict/', methods=['POST','GET']) 
def predict():
    if request.method == 'POST':
        V1 = request.form['V1']
        V2 = request.form['V2']
        V3 = request.form['V3']
        V4 = request.form['V4']
        V5 = request.form['V5']
        V6 = request.form['V6']
        V7 = request.form['V7']
        V8 = request.form['V8']
        x3 = [[V1, V2, V3, V4, V5, V6, V7, V8]]
        res = int(model.predict(x3))
        st = 'Soil_Type : ' + stdict[int(V4)]
        ct = 'Crop_Type: ' + ctdict[int(V5)]
        fr = 'Fertilizer_Required: ' + ferdict[int(res)]
        return render_template('result.html', _anchor='main', st=st, ct=ct, fr=fr)
    return render_template('predict.html', _anchor='main')

@app.route('/api',methods=['POST'])
def predictjson():
   data = request.get_json(force=True) 
   prediction = model.predict([np.array([data['V1'], data['V2'], data['V3'], data['V4'], data['V5'], data['V6'], data['V7'], data['V8']])])
   output = str(ferdict[int(prediction[0])]) + ',' + str(stdict[int(data['V4'])]) + ',' +str(ctdict[int(data['V5'])])
   return jsonify(output)

if __name__ == '__main__': 
   app.run(debug=True)