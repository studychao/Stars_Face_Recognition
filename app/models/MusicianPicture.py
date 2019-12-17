from app import db


class MusicianPicture(db.Model):
    __tablename__ = 'musicianpicture'
    ID = db.Column(db.INTEGER, primary_key=True)
    MID = db.Column(db.INTEGER)
    PictureUrl = db.Column(db.CHAR(255))
