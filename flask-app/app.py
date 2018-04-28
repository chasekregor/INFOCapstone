from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)

@app.route("/")
def home():


	movies = [
	{
		'title':'Saving Private Ryan',
		'average': 4
	},
	{
		'title':'Saving Private Ryan',
		'average': 4
	}
	]




	return render_template('home.html', movies = movies)

@app.route("/getresult",methods=['POST','GET'])
def get_result():
	if request.method=='POST':
		result=request.form








		return render_template('result.html',prediction=prediction)


@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
