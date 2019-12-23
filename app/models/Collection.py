from app import db


class Collection(db.Model):
    __tablename__ = 'collection'
    UID = db.Column(db.INTEGER, primary_key=True)
    MID = db.Column(db.INTEGER, primary_key=True)
    TimeStamp = db.Column(db.DateTime)
