from flask import Blueprint, request, jsonify
from app.services.user_service import conection_create_user, conection_get_users, conection_update_users
from app.controllers.user_controller import get_params_users
from app.database.db import db
from app.models.user_model import User


bp_route_user = Blueprint('bp_route_user', __name__)

@bp_route_user.route('/users', methods=['POST'])
def create_new_user():

    user_data = request.get_json()

    # Valida que no falten datos
    if not user_data or not 'name' in user_data or not 'email' in user_data or not 'password' in user_data:
        return jsonify({'error': 'Datos incompletos'}), 400

    db_response = conection_create_user(user_data)

    return db_response

@bp_route_user.route('/users', methods=['GET'])
def get_users():

    page, limit = get_params_users()

    try:
        page = int(page)
        limit = int(limit)

    except ValueError:
        return jsonify({'error': 'Error, parametros invalidos'}), 400

    users = conection_get_users(page, limit)

    if not users:
        return jsonify({'error':'Error, no se encontraron usuarios'}), 404

    return users

@bp_route_user.route('/users/<uid>', methods=['PATCH'])
def update_users(uid):

    if not uid:
        return jsonify({'error': 'Error, ingresar ID para validar el usuario'}), 400

    new_data_update = conection_update_users(uid)

    return new_data_update