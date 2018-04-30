from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.cluster import KMeans


app = Flask(__name__)


@app.route("/")
def home():



	pkl_file = open('movies', 'rb')
	movies = pickle.load(pkl_file)
	sampledmovies = np.random.choice(movies,500)




	return render_template('home.html', movies = sampledmovies)

@app.route("/result",methods=['POST','GET'])
def get_result():

	if request.method=='POST':
		result=request.form
		resultdict = dict(result)
		resulttitles=list(resultdict.keys())




		pkl_file = open('kmeans.pkl', 'rb')
		kmeansmodel = pickle.load(pkl_file)

		pkl_file = open('movies', 'rb')
		movies = pickle.load(pkl_file)

		predlist = []


		for c, i in enumerate(movies):
			if i in resulttitles:
				predlist.append(resultdict[i])
			else:
				predlist.append(movies[c]["average"])


		usercluster = kmeansmodel.predict([predlist])
		allratings = kmeansmodel.cluster_centers_[usercluster]

		sort_index = np.argsort(allratings[0])
		print(sort_index)
		print(allratings)
		top20 = sort_index[-31:-1]
		print(top20)

		prediction = []

		for i in top20:
			prediction.append(movies[i])

		print(prediction)

	return render_template('result.html',prediction=prediction, movies = movies)


@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/howitworks")
def howitworks():
	return render_template('howitworks.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
