from flask import render_template, request
from sqlalchemy import desc
from app.proto import bp
from app.models import Share


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    user_id = request.args.get('user_id')
    shares = Share.query.filter_by(user_id=user_id).order_by(desc(Share.timestamp)).all()
    return render_template('index.html', user_id=user_id, shares=shares)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')