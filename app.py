import numpy as np
import flask
from flask import Flask, request, jsonify, render_template
import os
import joblib
import xgboost
from xgboost.sklearn import XGBClassifier

model=joblib.load('demo_model.pkl')

app = Flask(__name__)

@app.route('/')
@app.route('/index')
# flask會到templates找
def home():
    return render_template('index.html')

@app.route('/predict_page.html',methods = ['GET','POST'])
def predict_page():
	return render_template("predict_page.html")

	
@app.route('/predict',methods=['POST'])
def predict():
	
	int_features = [int(x) for x in request.form.values()]
	final_features = np.array(int_features).reshape((1,-1))
	prob = model.predict(final_features)
	if int(prob)==1:
		prob_text = '判定此筆交易為盜刷'
	else:
		prob_text = '判定此筆交易非盜刷'
	return render_template('predict_page.html', prob_text=prob_text)

@app.route('/results',methods=['POST'])
def results():
	data = request.get_json(force=True)
	prediction = model.predict([np.array(list(data.values()))])

	prob = prediction[0]
	return jsonify(prob)
	
if __name__ == "__main__":
	app.run(debug = False, threaded=False)