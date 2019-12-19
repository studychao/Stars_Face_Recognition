from app import db


class Musician(db.Model):
    __tablename__ = 'musician'
    MID = db.Column(db.INTEGER, primary_key=True)
    Name = db.Column(db.CHAR(255))
    Birthday = db.Column(db.DateTime)
    Height = db.Column(db.INTEGER)
    RepresentativeWorks = db.Column(db.CHAR(255))
    MainAchievements = db.Column(db.CHAR(255))
