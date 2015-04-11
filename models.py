import datetime
from demo import db

class VarietyRank(db.Document):
    date = db.DateTimeField(required = True)
    rank = db.ListField(StringField, required = True)
    

