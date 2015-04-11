from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask('tv_media')
mongo = PyMongo(app)
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'tv_media'

from demo import views