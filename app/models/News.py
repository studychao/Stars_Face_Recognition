from app import db


class News(db.Model):
    __tablename__ = 'news'
    NID = db.Column(db.INTEGER, primary_key=True)
    Title = db.Column(db.CHAR(255))
    Content = db.Column(db.CHAR(255))
