from flask import Flask


def create_app():
    application = Flask(__name__)

    from app.proto import bp as proto_bp
    application.register_blueprint(proto_bp, url_prefix='/proto')

    return application