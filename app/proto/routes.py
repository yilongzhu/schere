from flask import current_app, render_template
from app.proto import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')