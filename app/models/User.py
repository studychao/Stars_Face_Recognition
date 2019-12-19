from app import db


class User(db.Model):
    __tablename__ = 'user'
    UID = db.Column(db.CHAR(255), primary_key=True)
    WechatName = db.Column(db.CHAR(255))
