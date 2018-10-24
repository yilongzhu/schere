from flask import render_template
from sqlalchemy import desc
from app.proto import bp
from app.models import Share


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    shares = Share.query.order_by(desc(Share.timestamp)).all()
    return render_template('index.html', shares=shares)