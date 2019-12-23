import datetime
from flask import Blueprint, request, jsonify
from .. import db
from ..models.Collection import Collection

mod_view = Blueprint('collection', __name__)


# 5查询用户收藏 input:用户id output:收藏列表
@mod_view.route('/collections', methods=['GET'])
def get_collections():
    uid = request.args.get('UID')
    collection_list = []
    collections = db.session.query(Collection.UID, Collection.MID, Collection.TimeStamp).filter(
        Collection.UID == uid).all()
    if collections is None:
        return None
    else:
        for collection in collections:
            data = {
                "MID": collection.MID,
                "UID": collection.UID,
                "TimeStamp": collection.TimeStamp
            }
            collection_list.append(data)
        return jsonify(collection_list)


# 3用户收藏歌手 input:用户ID,歌手ID,当前时间
@mod_view.route('/collection/add', methods=['POST'])
def add_collection():
    req_data = request.get_json()
    print(req_data)
    collection = Collection(UID=req_data["UID"], MID=req_data["MID"], TimeStamp=datetime.datetime.now())
    db.session.add(collection)
    db.session.commit()
    data = {
        "status": 1
    }
    return jsonify(data)


# 4判断用户是否收藏 input:歌手id,用户id output:T/F
@mod_view.route('/iscollection', methods=['GET'])
def is_collection():
    uid = request.args.get('UID')
    mid = request.args.get('MID')
    print(uid, mid)
    collection = db.session.query(Collection.UID, Collection.MID, Collection.TimeStamp).filter(Collection.UID == uid,
                                                                                               Collection.MID == mid).first()
    # user_info = db.session.query(User.UID).filter(User.WechatName == wechatname).first()
    if collection is None:
        data = {
            "status": 0
        }
        return jsonify(data)
    else:
        data = {
            "status": 1
        }
        return jsonify(data)


@mod_view.route('/delcollection', methods=['GET'])
def del_collection():
    """
    删除收藏
    :return: 状态1代表删除成功 状态2表示删除失败（collection信息不存在）
    """
    uid = request.args.get('UID')
    mid = request.args.get('MID')
    print(uid, mid)
    collection = db.session.query(Collection.UID, Collection.MID, Collection.TimeStamp).filter(Collection.UID == uid,
                                                                                               Collection.MID == mid).first()
    if collection is None:
        data = {
            "status": 0
        }
        return jsonify(data)
    else:
        db.session.query(Collection.UID, Collection.MID, Collection.TimeStamp).filter(Collection.UID == uid,
                                                                                      Collection.MID == mid).delete()
        db.session.commit()
        data = {
            "status": 1
        }
        return jsonify(data)
