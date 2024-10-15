from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.controllers.taxis_controller import get_params_taxis
from app.services.taxi_service import query_taxis

bp_route_taxis = Blueprint('bp_route_taxis', __name__)

@bp_route_taxis.route("/taxis", methods=['GET'])
@jwt_required()
def get_taxis() :

    page, per_page, plate, limit = get_params_taxis()

    taxis = query_taxis(page, per_page, plate, limit)

    if not taxis:
        return jsonify({'error': 'Error, no se encontraron Taxis'}), 404

    return jsonify(taxis), 200