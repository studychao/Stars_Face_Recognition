from flask import Blueprint, request, jsonify
from ..models.User import User
from .. import db
import datetime

mod_view = Blueprint('user', __name__)

# 添加用户 input:用户信息
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


# 查询 input:微信名 output:用户ID
@mod_view.route('/user', methods=['GET'])
def get_user_id():
    wechatname = request.args.get('wechatname')
    user_info = db.session.query(User.UID).filter(User.WechatName == wechatname).first()
    if user_info is None:
        return None
    else:
        data = {
            "UID": user_info[0]
        }
        return jsonify(data)

