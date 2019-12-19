from app import db


class User(db.Model):
    __tablename__ = 'user'
    UID = db.Column(db.INTEGER, primary_key=True)
    WechatName = db.Column(db.CHAR(255))
