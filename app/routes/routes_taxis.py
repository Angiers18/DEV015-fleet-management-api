from flask import Blueprint, request
from app.database.db import db
from app.models import Taxi

bp_route_taxis = Blueprint('bp_route_taxis', __name__)

@bp_route_taxis.route("/taxis", methods=['GET'])
def get_taxis() :

    """
    Obtiene una lista de taxis desde la base de datos con opciones de paginación y filtrado.

    La ruta responde a una solicitud GET y admite parámetros opcionales como `page`, `per_page`, 
    `plate`, y `limit` para controlar la paginación, el número de elementos por página, 
    la búsqueda por placa, y la cantidad máxima de resultados.

    Query Params:
        page (int, opcional): El número de página para la paginación (por defecto es 1).
        per_page (int, opcional): La cantidad de taxis por página (por defecto es 10).
        plate (str, opcional): Filtro para buscar taxis por matrícula usando coincidencia parcial.
        limit (int, opcional): El número máximo de taxis a devolver (por defecto es 10, entre 1 y 10).

    Returns:
        list[dict]: Una lista de diccionarios que representan cada taxi filtrado y paginado.
    """

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    plate = request.args.get('plate', '')

    query = db.session.query(Taxi) # inicia una consulta
    if plate:
        # like y % funcionan en sql verifica una secuencia de caracteres
        query = query.filter(Taxi.plate.like(f'%{plate}%'))

    limit = request.args.get('limit', )
    if limit:
        try:
            limit = int(limit)
            if limit < 1 or limit > 10:
                limit = per_page

        except ValueError:
            limit = per_page
    else:
        limit = per_page


    taxis = query.offset((page - 1) * per_page).limit(limit).all()

    # Obtiene total de resultados
    # total = query.count()

    return [taxi.to_dict() for taxi in taxis]