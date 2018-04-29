from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)

@app.route("/")
def home():



	pkl_file = open('movies', 'rb')
	movies = pickle.load(pkl_file)




	return render_template('home.html', movies = movies)

@app.route("/getresult",methods=['POST','GET'])
def get_result():
	if request.method=='POST':
		result=request.form
		day_of_week = result['day_of_week']

		pkl_file = open('cat', 'rb')
		index_dict = pickle.load(pkl_file)
		cat_vector = np.zeros(len(index_dict))


		pkl_file = open('kmeans.pkl', 'rb')
		kmeansmodel = pickle.load(pkl_file)

		try:
			cat_vector[index_dict['DAY_OF_WEEK_'+str(day_of_week)]] = 1
		except:
			pass


		usercluster = kmeansmodel.predict(cat_vector)
		allratings = kmeans.cluster_centers_[userscluster]

		sort_index = np.argsort(allratings)
		top20 = sort_index[-21:-1]

		movietitles = kmeansmodel.columns

		prediction = []

		for i in top20:
			prediction.append(movietitles[i])


		return render_template('result.html',prediction=prediction)


@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
