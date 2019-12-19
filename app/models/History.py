from app import db


class History(db.Model):
    __tablename__ = 'history'
    ID = db.Column(db.INTEGER, primary_key=True)
    UID = db.Column(db.INTEGER)
    MID = db.Column(db.INTEGER)
    TimeStamp = db.Column(db.DateTime)
    RecogPictureUrl = db.Column(db.CHAR(255))
