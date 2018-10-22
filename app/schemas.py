from app import ma
from app.models import Post

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post