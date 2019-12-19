from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(register_blueprint=True):
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)

    if register_blueprint:
        from .views import musician
        from .views import history
        from .views import news
        from .views import user
        app.register_blueprint(musician.mod_view)
        app.register_blueprint(history.mod_view)
        app.register_blueprint(news.mod_view)
        app.register_blueprint(user.mod_view)

    return app
