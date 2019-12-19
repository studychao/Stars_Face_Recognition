from flask import Blueprint, request, jsonify
from ..models.User import User
from .. import db
import datetime

mod_view = Blueprint('user', __name__)

# 查询 input:微信名 output:用户ID
@mod_view.route('/user', methods=['GET'])
def get_musician():
    wechatname = request.args.get('wechatname')
    user_info = db.session.query(User.UID).filter(User.WechatName == wechatname).first()
    # musician_info = db.session.query(Musician.Name, Musician.Birthday, Musician.Height, Musician.MainAchievements,
    #                                  Musician.RepresentativeWorks).filter(Musician.Name == name).first()
    if user_info is None:
        return None
    else:
        data = {
            "UID": user_info[0]
        }
        return jsonify(data)


# 插入收藏 input:MID UID
