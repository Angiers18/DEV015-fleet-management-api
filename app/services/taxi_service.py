from app.database.db import db
from app.models.taxi_model import Taxi

def query_taxis( page, per_page, plate, limit):

    """
    Consulta taxis en la base de datos con opciones de paginación y filtrado por placa.

    args:
        page (int, opcional): Número de la página solicitada para la paginación.
        per_page (int, opcional): Número de resultados por página.
        plate (str, opcional): Filtro por placa de taxi. Si se proporciona, buscará taxis cuyas placas contengan esta cadena.
        limit (int, opcional): Límite de resultados a devolver.

    returns:
        list: Una lista de diccionarios, donde cada diccionario representa los datos de un taxi.

    """

    query = db.session.query(Taxi) #inicia una consulta
    if plate:
        # like y % funcionan en sql verifica una secuencia de caracteres
        query = query.filter(Taxi.plate.like(f'%{plate}%'))


    taxis = query.offset((page - 1) * per_page).limit(limit).all()

    # Obtiene total de resultados
    # total = query.count()

    return [taxi.to_dict() for taxi in taxis]
