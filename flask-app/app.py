from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.cluster import KMeans


app = Flask(__name__)


@app.route("/")
def home():



	pkl_file = open('movies', 'rb')
	movies = pickle.load(pkl_file)
	sampledmovies = np.random.choice(movies,50)




	return render_template('home.html', movies = sampledmovies)

@app.route("/result",methods=['POST','GET'])
def get_result():

	if request.method=='POST':
		result=request.form

		print(" ")
		print("SHOWING RESULT")
		print(" ")
		print(result)
		#resultdict = dict(result)
		#resultdict = dict(result.values())



		#print("")
		#print("SHOWING RESULT TITLES")
		#print(resulttitles)
		#print("")


		with open('kmeans.pkl', 'rb') as fid:
			kmeansmodel = pickle.load(fid)


		#pkl_file = open('movies', 'rb')
		with open('movies','rb') as fid:
			movies = pickle.load(fid)

		print(movies)

		print(" ")
		print("PRINT OUT ALL MOVIES SHOW TO THE USER TO RATE")
		print(" ")

		resultdict = dict(result)

		print(resultdict)




		with open('movies_dict','rb') as fid:
			movies_dict = pickle.load(fid)

		all_user_avg = movies_dict

		cleanedresultdict = {}
		for m,v in resultdict.items():
			cleanedresultdict[m] = float(v[0])





		#resultdict = dict(result)
		all_user_avg.update(cleanedresultdict)
		predlist = list(all_user_avg.values())
		print("")
		print("PRITNING OUT PREDLIST")
		print("")
		print(predlist)







		usercluster = kmeansmodel.predict([predlist])
		allratings = kmeansmodel.cluster_centers_[usercluster]

		sort_index = np.argsort(allratings[0])
		#print(sort_index)
		#print(allratings)
		top30 = sort_index[-31:-1]
		#print(top30)

		prediction = []

		for i in top30:
			prediction.append(movies[i])

		return render_template('result.html',prediction=prediction, movies = movies)

"""
		for ix, moviedict in enumerate(movies):
			print(moviedict)
			if moviedict['title'] in resulttitles:
				predlist.append(resultdict[moviedict['title']])
			else:
				predlist.append(movies[ix]["average"])

		for c, i in enumerate(movies):
			if i in resulttitles:
				predlist.append(resultdict[i])
			else:
				predlist.append(movies[c]["average"])


		for c, i in enumerate(movies):
			if i['title'] in resulttitles:
				val = resultdict[i['title']][0]
				predlist.append(val)
			else:
				predlist.append(movies[c]["average"])"""











@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/howitworks")
def howitworks():
	return render_template('howitworks.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
