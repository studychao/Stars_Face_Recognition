from app import db


class Collection(db.Model):
    __tablename__ = 'user'
    UID = db.Column(db.INTEGER, primary_key=True)
    WechatName = db.Column(db.CHAR(255))
