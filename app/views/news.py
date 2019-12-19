from flask import Blueprint, request, jsonify
from ..models.News import News
from .. import db

mod_view = Blueprint('news', __name__)


@mod_view.route('/news/search', methods=['GET'])
def get_news():
    NID = request.args.get('NID')
    news_info = db.session.query(News.NID, News.Content, News.Title).filter(News.NID == NID).first()
    if news_info is None:
        return None
    else:
        data = {
            "NID": news_info[0],
            "Content": news_info[1],
            "Title": news_info[2]
        }
        return jsonify(data)


@mod_view.route('/news', methods=['GET'])
def get_news_all():
    news_dataset = []
    news_info = db.session.query(News.NID, News.Content, News.Title)
    for news in news_info:
        data = {
            "NID": news.NID,
            "Content": news.Content,
            "Title": news.Title
        }
        news_dataset.append(data)
        return jsonify(news_dataset)

