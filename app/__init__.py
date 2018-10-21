from flask import Flask
from config import Config


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)

    from app.proto import bp as proto_bp
    application.register_blueprint(proto_bp, url_prefix='/proto')

    return application