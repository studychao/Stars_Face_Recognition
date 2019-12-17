from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(register_blueprint=True):
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)

    if register_blueprint:
        from .views import view
        app.register_blueprint(view.mod_view)

    return app
