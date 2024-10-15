from sqlalchemy import func
from app.database.db import db
from app.models.trajectories_model import Trajectory

def conection_trajectories(taxi_id, date):

    """
    Consulta las trayectorias en la base de datos filtrando por ID del taxi y la fecha.

    args:
        taxi_id (int, requerido): Número único de cada taxi
        date (datetime, requerido): Fecha almacenada por ubicación

    returns:
        list: Una lista de diccionarios, donde cada diccionario representa las trayectorias de un taxi en una fecha específica.

    """

    query = db.session.query(Trajectory)

    trajectories = query.filter(
    Trajectory.taxi_id == taxi_id,
    func.date(Trajectory.date) == date.date()  # Comparar solo la fecha sin la hora
    ).all()

    return [trajectory.to_dict() for trajectory in trajectories]
