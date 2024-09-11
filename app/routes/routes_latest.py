from flask import Blueprint



bp_route_latest = Blueprint('bp_route_latest', __name__, url_prefix='/latest')

@bp_route_latest.route('/', methods=['GET'])
def get_lastest():
    return 'Holiis'

