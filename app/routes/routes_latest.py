from sqlalchemy import func
from flask import Blueprint, jsonify
from app.database.db import db
from app.models import Trajectory

bp_route_latest = Blueprint('bp_route_latest', __name__)

@bp_route_latest.route('/trajectories/latest', methods=['GET'])
def get_latest_trajectories():

         # Subconsulta que obtiene la última trayectoria por taxi_id
    subquery = db.session.query(
        Trajectory.taxi_id,
        func.max(Trajectory.date).label('latest_trajectories')
    ).group_by(Trajectory.taxi_id).subquery()

    latest = db.session.query(subquery).all()
    print('ultimas rutas y taxi_id', latest)

    latest_data = [{'taxi_id': row[0], 'latest_trajectories': row[1]} for row in latest]

    return jsonify(latest_data)
