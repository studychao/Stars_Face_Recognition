from app import db


class User(db.Model,):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.CHAR(100))
    Password = db.Column(db.CHAR(255))
    Authority = db.Column(db.INTEGER)
