from flask import Blueprint, request, jsonify
from app.services.user_service import conection_create_user


bp_route_user = Blueprint('bp_route_user', __name__)

@bp_route_user.route('/users', methods=['POST'])
def create_new_user():

    user_data = request.get_json()

    # Valida que no falten datos
    if not user_data or not 'name' in user_data or not 'email' in user_data or not 'password' in user_data:
        return jsonify({'error': 'Datos incompletos'}), 400

    db_response = conection_create_user(user_data)

    return db_response
