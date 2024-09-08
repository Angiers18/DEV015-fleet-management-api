from datetime import datetime
from flask import Blueprint, request, jsonify
from app.database.db import db
from app.models import Trajectory
from sqlalchemy import func


bp_route_trajectories = Blueprint('bp_route_trajectories', __name__)

@bp_route_trajectories.route("/trajectories", methods=['GET'])
def get_trajectories() :

    taxi_id = request.args.get('taxiId', '')
    if not taxi_id:
        return jsonify({"error": "El ID del taxi es obligatorio"}), 400

    date = request.args.get('date')

    if not date:
        return jsonify({"error": "La fecha es obligatoria"}), 400
    try:
       date = datetime.strptime(date, '%d-%m-%Y')

    except ValueError:
        return {'error': "Fecha invalida, por favor usa el formato DD-MM-YYYY"}, 400

    query = db.session.query(Trajectory)
    trajectories = query.filter(
    Trajectory.taxi_id == taxi_id,
    func.date(Trajectory.date) == date.date()  # Comparar solo la fecha
    ).all()

    if not trajectories:
        return jsonify({"error": "No se encontraron trayectorias para el taxi y fecha proporcionados"}), 404
    
    return jsonify([trajectory.to_dict() for trajectory in trajectories])
