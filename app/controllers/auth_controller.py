from flask import request
from flask_jwt_extended import create_access_token
from app.services.auth_service import check_user

def login_user():
    
    user_data = request.get_json()

    # Llama al servicio de autenticación
    find_user, error, status_code = check_user(user_data)

    if error:
        return error, status_code

    # Si la autenticación fue exitosa, genera el token de acceso
    access_token = create_access_token(identity=user_data['email'])
    
    return {
        'accessToken': access_token,
        'user': {
            'id': find_user.id,
            'email': find_user.email
        }
    }, 200
