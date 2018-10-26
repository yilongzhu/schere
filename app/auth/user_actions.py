from flask import redirect, url_for
from app import db
from app.models import User


def register_user(email, password):
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return redirect(route('proto.index', user_id=user.id))


def login_user(email, password):
    user = User.query.filter_by(email=email).first_or_404()
    if (user.check_password(password)):
        return redirect(url_for('proto.index', user_id=user.id))
    else:
        return redirect(url_for(proto.register))