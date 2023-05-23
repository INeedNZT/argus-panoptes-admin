VERSION = (0, 2)

__description__ = "The admin of Argus Panoptes"
__version__ = ".".join(map(str, VERSION))
__author__ = "Jingming Xia"
__email__ = "jingmingx01@gmail.com"
__license__ = "MIT License"


def create_app():
    from flask import Flask
    from flask_socketio import SocketIO
    app = Flask(__name__)
    add_config(app)
    register_database(app)
    regiser_jwt(app)
    register_log(app)
    regiser_routes(app)
    socketio = SocketIO(app, cors_allowed_origins='*')
    return app, socketio


def add_config(app):
    from . import settings
    app.config.from_object(settings.BasicConfig)
    app.config.from_object(settings.JWTConfig)
    mysql_config = settings.MySQLConfig()
    app.config.from_object(mysql_config)


def regiser_jwt(app):
    from flask_jwt_extended import JWTManager
    jwt = JWTManager(app)
    app.jwt = jwt


def register_log(app):
    from .utils.logger import get_logger
    app.logger = get_logger(app.db)


def register_database(app):
    from . import models
    db = models.db
    db.init_app(app)
    app.db = db
    # 创建数据库表
    with app.app_context():
        db.create_all()


def regiser_routes(app):
    from .admin import init_bp
    init_bp(app)
        


    