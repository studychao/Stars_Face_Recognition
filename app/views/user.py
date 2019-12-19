from flask import Blueprint, request, jsonify
from ..models.User import User
from .. import db

mod_view = Blueprint('user', __name__)


@mod_view.route('/user/add', methods=['POST'])
def add_user():
    req_data = request.get_json()
    user_info = db.session.query(User.UID, User.WechatName).filter(User.UID == req_data["UID"]).first()
    if user_info is None:
        user = User(UID=req_data["UID"], WechatName=req_data["WechatName"])
        db.session.add(user)
        db.session.commit()
        data = {
            "status": 1
        }
        return jsonify(data)
    else:
        data = {
            "status": 0
        }
        return jsonify(data)
