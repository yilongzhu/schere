from app import ma
from app.models import Share

class ShareSchema(ma.ModelSchema):
    class Meta:
        model = Share

share_schema = ShareSchema()
shares_schema = ShareSchema(many=True)