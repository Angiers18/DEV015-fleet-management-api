from flask import request

def get_params_taxis():

    """
    Obtiene los params:
        page (int, opcional): El número de página para la paginación (por defecto es 1)
        per_page (int, opcional): La cantidad de taxis por página (por defecto es 10)
        plate (str, opcional): Filtro para buscar taxis por matrícula usando coincidencia parcial
        limit (int, opcional): El número máximo de taxis por página (por defecto es 10, opcional entre 1 y 10)

    returns:
        params: page, per_page, plate, limit 
    """

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    plate = request.args.get('plate', '')

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

    return page, per_page, plate, limit