from flask import request

def get_params_users():

    page = request.args.get('page', 1)
    limit = request.args.get('limit', 10)

    return page, limit
