import bcrypt
from flask import jsonify, request
from app.database.db import db
from app.models.user_model import User

def connection_db_create_user(user_data):

    """
    consulta si el email ya existe en la base de datos y, si no existe, crea un nuevo usuario

    args:
        user_data (dict): Un diccionario con los datos del usuario, que debe incluir:
            name (str): El nombre del usuario
            email (str): El email del usuario
            password (str): La contraseña del usuario

    returns:
        retorna un diccionario con un mensaje de éxito y los datos del usuario (id, nombre, email)
    """

    # verifica si el email ya existe
    duplicate_email = User.query.filter_by(email=user_data['email']).first()

    if duplicate_email:
        return jsonify({"error": "El email ya existe"}), 409

    _password = user_data['password']
    hashed = bcrypt.hashpw(_password.encode('utf-8'), bcrypt.gensalt(12))

    # if bcrypt.checkpw(_password.encode('utf-8'), hashed):
    #     print('Match ^.^ ')
    # else:
    #     print('No match -.- ')


    # crea un nuevo usuario con los datos recibidos
    new_user = User(
        name=user_data['name'],
        email=user_data['email'],
        password=hashed.decode('utf-8')
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



def connection_db_get_users(page, limit):


    """
    Consulta usuarios en la base de datos con opciones de paginación y filtrado por placa.

    args:
        page (int): Número de la página solicitada para la paginación.
        limit (int): Límite de resultados a devolver.

    returns:
        list: Una lista de diccionarios, donde cada diccionario representa los datos de un usuario.
   """

    query = db.session.query(User)
    users = query.offset((page - 1) * limit).limit(limit).all()
    return jsonify([user.to_dict() for user in users])


def connection__db_update_users(uid):

    """
    Con el parámetro (uid) hace una consulta a la base de datos filtrando por el ID del usuario 
    y con los datos ingresados se actualiza la información del usuario.

    args:
        uid (int, requerido): Path param obligatorio, el ID del usuario a actualizar 

    returns:
         dict: un diccionario, que representa los datos del usuario.
   """
    user = db.session.query(User).filter_by(id=uid).first()

    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    data = request.get_json()


    if data:
        print('la data existe')
    else:
        print('la data no existe')
        return jsonify({'error': 'No se ingresaron datos para actualizar'}), 400


    if 'email' in data or 'password' in data:
        return jsonify({'error': 'Error, No esta permitido modificar el email o el password'}), 400

    if 'name' in data:
        user.name = data['name']

    try:
        db.session.commit()

        return jsonify({
            'message': 'Ususario actualizado con exito',
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200

    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': 'Error al actualizar el usuario', 'details': str(e)}), 500


def connection_db_delete_user(uid):

    """
    Con el parámetro (uid) hace una consulta a la base de datos filtrando por el ID del usuario y se elimina la información del usuario.

    args:
        uid (int, requerido): Path param obligatorio, el ID del usuario a actualizar 

    returns:
        dict: un diccionario, que representa el ID de usuario eliminado, el nombre y el email con el mensaje de eliminado
   """
    data_to_delete = db.session.query(User).filter_by(id=uid).first()

    if not data_to_delete:
        return jsonify({'error': 'Error, el usuario no existe'}), 404

    db.session.delete(data_to_delete)

    try:
        db.session.commit()
        return jsonify({
            'id': data_to_delete.id,
            'name': 'Nombre eliminado',
            'email': 'Email eliminado'
            }),200

    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': 'Error al eliminar al usuario', 'details': str(e)}), 500
