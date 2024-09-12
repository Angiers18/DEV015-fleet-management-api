from flask import Blueprint



bp_route_latest = Blueprint('bp_route_latest', __name__)

@bp_route_latest.route('/latest', methods=['GET'])
def get_lastest():
    return 'Holiis'

