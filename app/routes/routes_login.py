from flask import Blueprint
from app.controllers.login_controller import login_user


bp_route_login = Blueprint('bp_route_login', __name__)

@bp_route_login.route('/auth/login', methods=['POST'])
def login():

    return login_user()
