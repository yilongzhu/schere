from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
socketio = SocketIO()

def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)

    db.init_app(application)
    migrate.init_app(application, db)
    ma.init_app(application)
    socketio.init_app(application)

    from app.proto import bp as proto_bp
    application.register_blueprint(proto_bp, url_prefix='/proto')
    from app.api import bp as api_bp
    application.register_blueprint(api_bp, url_prefix='/api')

    return application


from app import models