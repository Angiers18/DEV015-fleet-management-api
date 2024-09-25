from flask import request

def get_params_users():
    """ 
    Obtiene los params:
        page (int, opcional): El número de página para la paginación (por defecto es 1)
        limit (int, opcional): El número máximo de usuarios por página (por defecto es 10, opcional entre 1 y 10)

    returns:
        params: page, per_page, plate, limit 
        longitude (float): longitud de la última ubicación registrada
    """
    page = request.args.get('page', 1)
    limit = request.args.get('limit', 10)

    return page, limit
