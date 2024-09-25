from flask import Blueprint, jsonify
from app.services.latest_service import query_latest
from app.controllers.latest_controller import dict_latest_trajectories


bp_route_latest = Blueprint('bp_route_latest', __name__)

@bp_route_latest.route('/trajectories/latest', methods=['GET'])
def get_latest_trajectories():

    last_trajectories = query_latest()

    if not last_trajectories:
        return jsonify({ "error": "Ultimas rutas no encontradas" }), 404

    latest_trajectories = dict_latest_trajectories(last_trajectories)

    return jsonify(latest_trajectories), 200
