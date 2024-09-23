from flask import jsonify
from app.database.db import db
from app.models.user_model import User

def conection_create_user(user_data):

    """
    consulta si el email ya existe en la base de datos y, si no existe, crea un nuevo usuario

    args:
        user_data (dict): Un diccionario con los datos del usuario, que debe incluir:
            name (str): El nombre del usuario
            email (str): El email del usuario
            password (str): La contraseña del usuario

    returns:
            si el email ya existe, retorna un mensaje de error
            si el usuario es creado exitosamente, retorna un diccionario con un mensaje de éxito y los datos del usuario (id, nombre, email)
            si ocurre un error al guardar en la base de datos, retorna un mensaje de error detallando la causa
   
    """

    # verifica si el email ya existe
    duplicate_email = User.query.filter_by(email=user_data['email']).first()

    if duplicate_email:
        return jsonify({"error": "El email ya existe"}), 409

    # crea un nuevo usuario con los datos recibidos
    new_user = User(
        name=user_data['name'],
        email=user_data['email'],
        password=user_data['password']
    )

    db.session.add(new_user)

    try:
        db.session.commit()
        return jsonify({
            'message': 'Usuario agregado exitosamente',
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email
        }), 201

    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': 'Error al crear el usuario', 'details': str(e)}), 500



def conection_get_users(page, limit):

    query = db.session.query(User)
    users = query.offset((page - 1) * limit).limit(limit).all()
    return jsonify([user.to_dict() for user in users])
