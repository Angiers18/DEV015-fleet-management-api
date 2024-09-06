from flask import Blueprint, request
from datetime import datetime
from app.database.db import db
from app.models import Trajectory

bp_route_trajectories = Blueprint('bp_route_trajectories', __name__)

@bp_route_trajectories.route("/trajectories", methods=['GET'])
def get_trajectories() :

    taxi_id = (request.args.get('taxiId', ))

    trajectories = db.session.query(Trajectory).filter_by(taxi_id=taxi_id).all()

    return [trajectory.to_dict() for trajectory in trajectories]
