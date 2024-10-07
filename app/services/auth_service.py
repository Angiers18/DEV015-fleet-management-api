import bcrypt
from app.models.user_model import User

def check_user(user_data):

    if not 'email' in user_data or not 'password' in user_data:
        return None, {'error': 'Falta usuario o password'}, 400

    find_user = User.query.filter_by(email=user_data['email']).first()

    if not find_user:
        return None, {'error': 'Usuario no encontrado'}, 404

    if not bcrypt.checkpw(user_data['password'].encode('utf-8'), find_user.password.encode('utf-8')):
        print('password no coincide -.-')
        return None, {'error': 'Password invalida'}, 404

    print('password coincide')
    return find_user, None, 200