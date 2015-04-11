from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
app.config['MONGO_DBNAME'] = 'tv_media'

if __name__ == '__main__':
    app.run()