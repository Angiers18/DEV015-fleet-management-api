from flask import Blueprint

bp_route_home = Blueprint('bp_route_home', __name__)

@bp_route_home.route("/")
def hello() :
    return "Hola mundo!!"
