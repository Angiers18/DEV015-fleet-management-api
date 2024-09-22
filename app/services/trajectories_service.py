from sqlalchemy import func
from app.database.db import db
from app.models.trajectories_model import Trajectory

def conection_trajectories(taxi_id, date):

    """
    consulta taxis en la base de datos con opciones de paginación y filtrado por placa.

    args:
        page (int): numero de la pagina solicitada para la paginación
        per_page (int): numero de resultados por pagina
        plate (str, opcional): filtro por placa de taxi, si se proporciona, buscara taxis cuyas placas contengan esta cadena
        limit (int): limite de resultados a devolver

    returns:
        list: Una lista de diccionarios, donde cada diccionario representa los datos de un taxi.

    """

    query = db.session.query(Trajectory)

    trajectories = query.filter(
    Trajectory.taxi_id == taxi_id,
    func.date(Trajectory.date) == date.date()  # Comparar solo la fecha sin la hora
    ).all()

    return [trajectory.to_dict() for trajectory in trajectories]
