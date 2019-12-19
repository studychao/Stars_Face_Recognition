from flask import Blueprint, request, jsonify
from .. import db
from ..models.History import History

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