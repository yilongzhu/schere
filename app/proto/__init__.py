from flask import Blueprint

bp = Blueprint('proto', __name__)

from app.proto import routes