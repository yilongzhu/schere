import json
from flask import render_template, request, redirect, url_for, jsonify
from flask_socketio import emit, send
from sqlalchemy import desc
from app import db, socketio
from app.proto import bp
from app.models import Share
from app.schemas import share_schema


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    shares = Share.query.order_by(desc(Share.timestamp)).all()
    return render_template('index.html', shares=shares)


@socketio.on('user_connect')
def user_connect(message):
    print("User connected: " + message)

@socketio.on('new_share')
def new_share(message):
    print("New share: " + message)
    new_share = Share(body=message)
    db.session.add(new_share)
    db.session.commit()
    print("Tuple committed")
    emit('response', share_schema.dump(new_share), json=True, broadcast=True)