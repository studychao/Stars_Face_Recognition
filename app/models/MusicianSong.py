from app import db


class MusicianSong(db.Model):
    __tablename__ = 'musiciansong'
    MID = db.Column(db.INTEGER, primary_key=True)
    AlbumName = db.Column(db.CHAR(255))
    AlbumPictureUrl = db.Column(db.CHAR(255))
    SongName = db.Column(db.CHAR(255), primary_key=True)
    SongUrl = db.Column(db.CHAR(255))
