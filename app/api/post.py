from flask import jsonify
from app import db
from app.api import bp
from app.models import Post
from app.schemas import PostSchema

post_schema = PostSchema()


@bp.route('/post/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post_schema.dump(post).data)