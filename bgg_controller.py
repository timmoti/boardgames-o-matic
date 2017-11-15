import flask
import pickle
import pandas as pd
import numpy as np


#------ CONFIG ------ #
app = flask.Flask(__name__)

#-----MODEL--------#

df = pd.read_pickle('../ratings_pickle')
games = pd.read_csv('../bgg_gamelist.csv')
svd50preds = pd.read_pickle('../svd50preds_pickle')
all_sims = pd.read_pickle('../cos_ii_sims_all_pickle')
alspreds = pd.read_pickle('../alspreds_pickle')

#----- ROUTES -------#
@app.route("/")
def home():
	return flask.redirect("/home")
	
@app.route("/home")
def predict():
	algo = 'abc'
	return flask.render_template("bgg_input.html", algo=algo)

@app.route('/result', methods=['POST', 'GET'])
def recommend():

	user = flask.request.form['user']
	if user not in df.index:
		return flask.render_template('bgg_error.html')
	algo = flask.request.form['algo']
	algo_list = []
	with open('result.txt', 'rb') as r:
		for line in r:
			if line.split(',')[0] == user:
				alg = line.split(',')[1]
				if alg in algo_list:
					pass
				else:
					algo_list.append(alg)

	not_done = True

	if len(algo_list) == 0 or algo == '1':
		if algo == '1':
			not_done = False
		algorithm = 'Singular Value Decomposition'
		algo = 'svd'
		user_idx = df.index.get_loc(user)
		prediction = svd50preds[user_idx]
		rated = df.loc[user].fillna(0).as_matrix().nonzero()

		mask = np.ones_like(prediction, dtype=bool)
		mask[rated] = False
		prediction[~mask] = 0

	elif len(algo_list) == 1 or algo == '2':
		if algo == '2':
			not_done = False
		algorithm = 'Non-Negative Matrix Factorization with Weighted Alternating Least Squares'	
		algo = 'als'
		user_idx = df.index.get_loc(user)
		prediction = alspreds[user_idx]
		rated = df.loc[user].fillna(0).as_matrix().nonzero()

		mask = np.ones_like(prediction, dtype=bool)
		mask[rated] = False
		prediction[~mask] = 0

	elif len(algo_list) == 2 or algo == '3' :
		if algo == '3':
			not_done = False
		algorithm = "Cosine Similarity"
		algo = 'cos'
		prediction = np.zeros_like(df.loc[user])
		ratings_array = df.fillna(0).as_matrix()
   		person = ratings_array[df.index.get_loc(user)]
   		rated = person.nonzero()[0]
	   	for idx in range(ratings_array.shape[1]):
	   		if idx not in rated:
	   			sim = all_sims[idx]
	   			prediction[idx] = np.sum(sim[rated]*person[rated])/np.sum(np.abs(sim[rated]))

	elif len(algo_list) == 3:
		return flask.render_template('bgg_last.html', user=user)

	

	predictions = pd.Series(prediction, index=df.columns, name='predictions')
	recommendations = games.join(predictions, on='gameid')
	recommendation = recommendations.sort_values('predictions', ascending=False).head(20)
	recommendation = recommendation[['gamename', 'gamerank']].rename(columns={'gamename': 'Game Title', 'gamerank': 'BGG Rank'})
	recommendation = recommendation.reset_index(drop=True)
	return flask.render_template('bgg_results.html', user=user, algorithm=algorithm, algo=algo,
		tables=[recommendation.to_html(classes='recommendation', index=False)], titles=['na', 'Recommended based on your ratings'], not_done=not_done)



@app.route('/about')
def about():
	return flask.render_template('bgg_about.html')

@app.route('/contact')
def contact():
	return flask.render_template('bgg_contact.html')

@app.route('/feedback', methods = ['POST', 'GET'])
def feedback():
    if flask.request.method == 'POST':
    	user = flask.request.form['username']
        fdbk = flask.request.form['feedback_input']  

    with open('feedback.txt','a') as f:
        f.write(user + ',')
        f.write(fdbk + '\n')

    return flask.render_template('bgg_feedback.html')

@app.route('/rating', methods = ['POST', 'GET'])
def rating():
	if flask.request.method == 'POST':
		if flask.request.form['submit'] == 'good':
			rating = 1
		elif flask.request.form['submit'] == 'not_good':
			rating = 0
		else:
			pass
	user = flask.request.form['user']
	algorithm = flask.request.form['algorithm']
	algo = flask.request.form['algo']

	with open('result.txt', 'a') as r:
		r.write(user + ',')
		r.write(algo + ',')
		r.write(str(rating) + '\n')

	if algo == 'cos':
		return flask.render_template('bgg_last.html', user=user, algorithm=algorithm, algo=algo)
	else:
		return flask.render_template('bgg_rating.html', user=user, algorithm=algorithm, algo=algo)	

@app.route('/last', methods = ['POST', 'GET'])
def last():
	user = flask.request.form['user']
	return flask.render_template('bgg_last.html', user=user)	
	

#------ MAIN SENTINEL ------#
if __name__ == '__main__':
	app.run(threaded=True)
