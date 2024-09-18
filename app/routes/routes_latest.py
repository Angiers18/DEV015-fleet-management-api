from sqlalchemy import func
from flask import Blueprint, jsonify
from app.database.db import db
from app.models import Trajectory, Taxi

bp_route_latest = Blueprint('bp_route_latest', __name__)

@bp_route_latest.route('/trajectories/latest', methods=['GET'])
def get_latest_trajectories():

    # Subconsulta que obtiene la última trayectoria por taxi_id
    subquery = db.session.query(
        Trajectory.taxi_id,
        #func max (funcion de sql) .label(renombra el resultado de una función)
        func.max(Trajectory.date).label('latest_trajectories')
        #group_by (agrupa los resultados de cada taxi con su ultima trayectoria)
    ).group_by(Trajectory.taxi_id).subquery()

    last_trajectories = db.session.query(
        Taxi.id,
        Taxi.plate,
        Trajectory.date,
        Trajectory.latitude,
        Trajectory.longitude
    ).join(Trajectory, Taxi.id == Trajectory.taxi_id)\
    .filter(Trajectory.taxi_id == subquery.c.taxi_id)\
    .filter(Trajectory.date == subquery.c.latest_trajectories).distinct()\
    .all()

    if not last_trajectories:
        return jsonify({ "error": "Ultimas rutas no encontradas" }), 404

    dict_latest_trajectories = []
    for trajectory in last_trajectories:
        dict_latest_trajectories.append({
            'taxiId': trajectory.id,              # Taxi ID
            'plate': trajectory.plate,            # Placa del taxi
            'timestamp': trajectory.date,         # Fecha de la última trayectoria
            'latitude': trajectory.latitude,      # Latitud
            'longitude': trajectory.longitude     # Longitud
        })

    return jsonify(dict_latest_trajectories), 200
