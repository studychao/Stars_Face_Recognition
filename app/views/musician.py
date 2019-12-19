from flask import Blueprint, request, jsonify
from ..models.Musician import Musician
from .. import db

mod_view = Blueprint('musician', __name__)


@mod_view.route('/musician', methods=['GET'])
def get_musician():
    name = request.args.get('name')
    musician_info = db.session.query(Musician.Name, Musician.Birthday, Musician.Height, Musician.MainAchievements,
                                     Musician.RepresentativeWorks).filter(Musician.Name == name).first()
    if musician_info is None:
        return None
    else:
        data = {
            "Name": musician_info[0],
            "Birthday": musician_info[1],
            "Height": musician_info[2],
            "MainAchievements": musician_info[3],
            "RepresentativeWorks": musician_info[4]
        }
        return jsonify(data)
