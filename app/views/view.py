from flask import Blueprint

mod_view = Blueprint('view', __name__)

@mod_view.route('/hello', methods=['GET'])
def hello():
    return "hello"