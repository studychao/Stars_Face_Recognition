from app import db


class MusicianSong(db.Model):
    __tablename__ = 'musiciansong'
    ID = db.Column(db.INTEGER, primary_key=True)
    MID = db.Column(db.INTEGER)
    AlbumName = db.Column(db.CHAR(255))
    AlbumPictureUrl = db.Column(db.CHAR(255))
    SongName = db.Column(db.CHAR(255))
    SongUrl = db.Column(db.CHAR(255))
