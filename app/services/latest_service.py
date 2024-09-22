from sqlalchemy import func
from app.database.db import db
from app.models.taxi_model import Taxi
from app.models.trajectories_model import Trajectory

def query_latest():

    """
    se realiza una subconsulta a la base de datos para obtener la última 
    ubicación registrada (trayectoria) de cada taxi en el sistema

    utiliza una consulta para obtener la última trayectoria de cada taxi, y luego 
    consulta los detalles de la trayectoria, incluyendo la fecha, latitud y longitud

    returns:
        list: Una lista de objetos con la data
        
        'id'(int) id del taxi,
        'plate'(int) placa del taxi,
        'date' (datetime) fecha de la última trayectoria,
        'latitude' latitud de la última ubicación registrada,
        'longitude' longitud de la última ubicación registrada
        
    """
# Subconsulta que obtiene la última trayectoria por taxi_id
    subquery = db.session.query(
        Trajectory.taxi_id,
        #func max (funcion de sql) .label(renombra el resultado de la función)
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

    return last_trajectories