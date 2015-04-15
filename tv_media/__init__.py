from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
app.config['MONGO_HOST'] = '202.120.38.146'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'tv_media'

from tv_media import views

if __name__ == "__main__":
    app.run()
