from flask import render_template
from demo import app,mongo


@app.route('/variety/<date>')
def variety_rank(date):
	rank = mongo.db.variety_rank.find_one_or_404({'date':date}, {'rank':1, '_id':0})['rank']
	return render_template('variety_rank.html', rank = rank, date = date)

@app.route('/drama/<date>')
def drama_rank(date):
	rank = mongo.db.drama_rank.find_one_or_404({'date':date}, {'rank':1, '_id':0})['rank']
	return render_template('drama_rank.html', rank = rank, date = date)