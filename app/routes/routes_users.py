from flask import Blueprint, jsonify, request
from app.models import User
from app.database.db import db


bp_route_user = Blueprint('bp_route_user', __name__)

@bp_route_user.route('/users', methods=['POST'])
def create_new_user():

    user_data = request.get_json()  # obtiene los datos del body_request en (JSON)

    # valida que no falten datos
    if not 'name' in user_data or not 'email' in user_data or not 'password' in user_data:
        return jsonify({'error': 'Datos incompletos'}), 400

    duplicate_email = User.query.filter_by(email=user_data['email']).first()

    if duplicate_email:
        return jsonify({"error": "El email ya existe"}), 409

    # une la data obtenida del ususario con las column de la db
    new_user = User(
        name = user_data['name'],
        email = user_data['email'],
        password = user_data['password']
    )

    db.session.add(new_user) #agrega el nuevo usuario

    try:
        db.session.commit()
        return jsonify({'message': 'Usuario agregado exitosamente',
                        'id': new_user.id,
                        'name': new_user.name,
                        'email': new_user.email
                        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al crear el usuario', 'details': {str(e)}}), 500
