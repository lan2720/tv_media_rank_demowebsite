#coding:utf-8

from flask import render_template,request
from tv_media import app,mongo
import datetime

@app.route('/', methods = ['GET'])
def rank():
	date = request.args.get('date','')
	today = datetime.datetime.now().strftime("%Y-%m-%d")
	if not date or date == today: # 如果get到了日期, 则查询相应日期数据
		istoday = True
	else:
		istoday = False
	if not date:
		date = today

	variety = mongo.db.variety_rank.find_one({'date':date}, {'rank':1, '_id':0})
	drama = mongo.db.drama_rank.find_one({'date':date}, {'rank':1, '_id':0})
	station = mongo.db.station_rank.find_one({'date':date}, {'rank':1, '_id':0})
	if variety:
		variety_rank = variety['rank']
	else:
		variety_rank = []
	if drama:
		drama_rank = drama['rank']
	else:
		drama_rank = []
	if station:
		station_rank = station['rank']
	else:
		station_rank = []

	pre = (datetime.datetime.strptime(date,"%Y-%m-%d") + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
	nextday = (datetime.datetime.strptime(date,"%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
	return render_template('rank.html', variety_rank = variety_rank, drama_rank = drama_rank, tv_rank = station_rank, date = date, istoday = istoday, pre = pre, next = nextday)

@app.route('/drama', methods = ['GET'])
def drama_rank_detail():
	date = request.args.get('date','')
	drama = mongo.db.drama_rank.find_one({'date':date}, {'rank':1, '_id':0})
	if drama:
		drama_rank = drama['rank']
	else:
		drama_rank = []
	return render_template('drama_rank.html', drama_rank = drama_rank)

@app.route('/variety', methods = ['GET'])
def variety_rank_detail():
	date = request.args.get('date','')
	variety = mongo.db.variety_rank.find_one({'date':date}, {'rank':1, '_id':0})
	if variety:
		variety_rank = variety['rank']
	else:
		variety_rank = []
	return render_template('variety_rank.html', variety_rank = variety_rank)

@app.route('/tv', methods = ['GET'])
def station_rank_detail():
	date = request.args.get('date','')
	station = mongo.db.station_rank.find_one({'date':date}, {'rank':1, '_id':0})
	if station:
		station_rank = station['rank']
	else:
		station_rank = []
	return render_template('tv_rank.html', tv_rank = station_rank)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

