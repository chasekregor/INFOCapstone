from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/getresult",methods=['POST','GET'])
def get_result():
	if request.method=='POST':
		result=request.form
		return render_template('result.html',prediction=prediction)
		




if __name__ == '__main__':
	app.debug = True
	app.run()
