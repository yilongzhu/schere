from flask import jsonify
from app import db
from app.api import bp
from app.models import Share
from app.schemas import share_schema, shares_schema


@bp.route('/shares/<int:id>', methods=['GET'])
def get_share(id):
    share = Share.query.get_or_404(id)
    return jsonify(share_schema.dump(share).data)


@bp.route('/shares', methods=['GET'])
def get_shares():
    shares = Share.query.all()
    print(shares)
    return jsonify(shares_schema.dump(shares).data) 