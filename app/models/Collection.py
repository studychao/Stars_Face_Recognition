from app import db


class Collection(db.Model):
    __tablename__ = 'collection'
    ID = db.Column(db.INTEGER, primary_key=True)
    UID = db.Column(db.INTEGER)
    MID = db.Column(db.INTEGER)
    TimeStamp = db.Column(db.Datetime)
