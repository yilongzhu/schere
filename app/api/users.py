from flask import jsonify, request

from app import db
from app.api import bp
from app.auth import user_actions
from app.models import User
from app.schemas import user_schema, users_schema

from webargs import fields, validate
from webargs.flaskparser import use_args


user_args = {
    'email': fields.Str(required=True),
    'password': fields.Str(required=True, validate=validate.Length(min=6))
}

@bp.route('/register', methods=['POST'])
@use_args(user_args)
def register_user(args):
    return user_actions.register_user(
        args['email'],
        args['password']
    )


@bp.route('/login', methods=['POST'])
@use_args(user_args)
def login_user(args):
    return user_actions.login_user(
        args['email'],
        args['password']
    )


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user_schema.dump(user).data)


@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users).data) 