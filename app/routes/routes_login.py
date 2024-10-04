from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from app.models.user_model import User
import bcrypt

bp_route_login = Blueprint('bp_route_login', __name__)

@bp_route_login.route('/auth/login', methods=['POST'])
def login_users():

    user_data = request.get_json()

    if not 'email' in user_data or not 'password' in user_data:
        return ({'error': 'Usuario o contraseña incorrectos'}), 400


    find_user = User.query.filter_by(email=user_data['email']).first()

    if not find_user:
        return ({'error': 'Usuario no encontrado'}), 404

    if not bcrypt.checkpw(user_data['password'].encode('utf-8'), find_user.password.encode('utf-8')):

        print('password not mach -.-')
        return ({'error': 'Password invalida'}), 404


    print('password mach')
    access_token = create_access_token(identity=user_data['email'])
    return ({'accessToken': access_token,
                    'user':{
                            'id': find_user.id,
                            'email': find_user.email
                            }
                    }), 200
