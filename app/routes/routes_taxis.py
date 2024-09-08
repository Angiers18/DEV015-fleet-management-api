from flask import Blueprint, request
from app.database.db import db
from app.models import Taxi

bp_route_taxis = Blueprint('bp_route_taxis', __name__)

@bp_route_taxis.route("/taxis", methods=['GET'])
def get_taxis() :

    #paginacion
    page = int(request.args.get('page', 1)) #una pagina
    per_page = int(request.args.get('per_page', 10)) #diez elementos por pagina
    plate = request.args.get('plate', '') # queryparams

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