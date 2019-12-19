from app import db


class History(db.Model):
    __tablename__ = 'history'
    UID = db.Column(db.INTEGER, primary_key=True)
    MID = db.Column(db.INTEGER, primary_key=True)
    TimeStamp = db.Column(db.DateTime, primary_key=True)
    RecogPictureUrl = db.Column(db.CHAR(255))
