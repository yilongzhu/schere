from flask_socketio import emit, join_room
from app import db, socketio
from app.models import Share
from app.schemas import share_schema


@socketio.on('user_connect')
def user_connect():
    print("SocketIO: User connected")


@socketio.on('user_login')
def user_login(user_id):
    join_room(user_id)
    print('SocketIO: Joined room \"' + user_id + '\"')


@socketio.on('new_share')
def new_share(data):
    print('SocketIO: New share \"' + data['share'] + '\"')
    new_share = Share(body=data['share'])
    db.session.add(new_share)
    db.session.commit()
    emit('response', share_schema.dump(new_share), json=True, room=data['user_id'])