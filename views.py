from flask import render_template,request
from demo import app,mongo


@app.route('/variety/<date>')
def variety_rank(date):
	rank = mongo.db.variety_rank.find_one_or_404({'date':date}, {'ranks':1, '_id':0})
	return render_template('variety_rank.html', rank = rank, date = date)

    