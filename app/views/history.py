from flask import Blueprint, request, jsonify
from .. import db
from ..models.History import History
import datetime

mod_view = Blueprint('history', __name__)


@mod_view.route('/history/detail', methods=['GET'])
def history_detail():
    UID = request.args.get('UID')
    MID = request.args.get('MID')
    history_info = db.session.query(History.MID, History.UID, History.TimeStamp, History.RecogPictureUrl).filter(
        History.UID == UID, History.MID == MID).first()
    if history_info is None:
        return None
    else:
        data = {
            "MID": history_info[0],
            "UID": history_info[1],
            "TimeStamp": history_info[2],
            "RecogPictureUrl": history_info[3],
        }
        return jsonify(data)


@mod_view.route('/history/search', methods=['GET'])
def history_search():
    UID = request.args.get('UID')
    history_dataset = []
    history_info = db.session.query(History.MID, History.UID, History.TimeStamp, History.RecogPictureUrl).filter(
        History.UID == UID)
    if history_info is None:
        return None
    else:
        for history in history_info:
            data = {
                "MID": history.MID,
                "UID": history.UID,
                "TimeStamp": history.TimeStamp,
                "RecogPictureUrl": history.RecogPictureUrl
            }
            history_dataset.append(data)
        return jsonify(history_dataset)


# 6添加用户历史记录 input:用户ID,歌手ID,当前时间,已识别图片URL
@mod_view.route('/history/add', methods=['POST'])
def add_history():
    req_data = request.get_json()
    history = History(UID=req_data["UID"], MID=req_data["MID"], TimeStamp=datetime.datetime.now(), RecogPictureUrl=req_data["RecogPictureUrl"])
    db.session.add(history)
    db.session.commit()
    data = {
        "status": 1
    }
    return jsonify(data)
