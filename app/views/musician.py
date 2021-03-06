from flask import Blueprint, request, jsonify
from ..models.Musician import Musician
from ..models.MusicianPicture import MusicianPicture
from ..models.MusicianSong import MusicianSong
from .. import db

mod_view = Blueprint('musician', __name__)


# 2歌手详情 input:歌手名 output:歌手信息
@mod_view.route('/musician', methods=['GET'])
def get_musician():
    name = request.args.get('name')
    musician_info = db.session.query(Musician.Name, Musician.Birthday, Musician.Height, Musician.MainAchievements,
                                     Musician.RepresentativeWorks, Musician.MID).filter(Musician.Name == name).first()
    if musician_info is None:
        return None
    else:
        mid = musician_info[5]
        song_list = []
        pic_list = []
        musician_song = db.session.query(MusicianSong.AlbumName, MusicianSong.AlbumPictureUrl, MusicianSong.SongName,
                                         MusicianSong.SongUrl).filter(MusicianSong.MID == mid).all()
        if musician_song:
            for i in musician_song:
                song_list.append(i)

        musician_pic = db.session.query(MusicianPicture.PictureUrl).filter(MusicianPicture.MID == mid).all()
        if musician_pic:
            for j in musician_pic:
                pic_list.append(j)
        data = {
            "Name": musician_info[0],
            "Birthday": musician_info[1].strftime('%Y-%m-%d'),
            "Height": musician_info[2],
            "MainAchievements": musician_info[3],
            "RepresentativeWorks": musician_info[4],
            "Songs": song_list,
            "Pictures": pic_list
        }
        return jsonify(data)


# 1搜索歌手 input:歌手名（模糊匹配） output:歌手列表
@mod_view.route('/musicians', methods=['GET'])
def search_musicians():
    name = request.args.get('name')
    musicians_info = db.session.query(Musician.Name).filter(
        Musician.Name.like("%" + name + "%") if name is not None else ""
        # Students.remark.like("%" + key_remark + "%") if key_remark is not None else ""
    ).all()
    data_list = list()
    if musicians_info:
        for i in musicians_info:
            name = i[0]
            data_list.append(name)

        return jsonify(data_list)
