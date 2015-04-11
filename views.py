from flask import render_template
from demo import app,mongo


@app.route('/variety/<date>')
def variety_rank(date):
	try:
		rank = mongo.db.variety_rank.find_one({'date':date}, {'rank':1, '_id':0})['rank']
	except Exception:
		rank = []
	finally:
		return render_template('variety_rank.html', rank = rank, date = date)

@app.route('/drama/<date>')
def drama_rank(date):
	try:
		rank = mongo.db.drama_rank.find_one_or_404({'date':date}, {'rank':1, '_id':0})['rank']
	except Exception:
		rank = []
	finally:
		return render_template('drama_rank.html', rank = rank, date = date)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404