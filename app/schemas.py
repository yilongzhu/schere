from app import ma
from app.models import User, Share


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

class ShareSchema(ma.ModelSchema):
    class Meta:
        model = Share


user_schema = UserSchema()
users_schema = UserSchema(many=True)

share_schema = ShareSchema()
shares_schema = ShareSchema(many=True)