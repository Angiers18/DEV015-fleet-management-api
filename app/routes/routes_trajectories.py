from datetime import datetime
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.controllers.trajectories_controller import get_params_trajectories
from app.services.trajectories_service import conection_trajectories

bp_route_trajectories = Blueprint('bp_route_trajectories', __name__)

@bp_route_trajectories.route("/trajectories", methods=['GET'])
@jwt_required()
def get_trajectories():

    taxi_id, date = get_params_trajectories()

    if not taxi_id:
        return jsonify({"error": "El ID del taxi es obligatorio"}), 400

    if not date:
        return jsonify({"error": "La fecha es obligatoria"}), 400
    try:
        date = datetime.strptime(date, '%d-%m-%Y')

    except ValueError:
        return jsonify({"error": "Fecha invalida, por favor usa el formato DD-MM-YYYY"}), 400
    trajectories = conection_trajectories(taxi_id, date)

    if not trajectories:
        return jsonify({"error": "No se encontraron trayectorias para el taxi y fecha proporcionados"}), 404
    
    return jsonify(trajectories), 200
