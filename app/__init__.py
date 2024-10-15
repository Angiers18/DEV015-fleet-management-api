# Este file inicializa la aplicación Flask
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from app.config import Config
from app.database.db import db

from app.routes.routes_taxis import bp_route_taxis
from app.routes.routes_home import bp_route_home
from app.routes.routes_trajectories import bp_route_trajectories
from app.routes.routes_latest import bp_route_latest
from app.routes.routes_users import bp_route_user
from app.routes.routes_login import bp_route_login



def create_app(config_ = Config):
    app = Flask(__name__)
    app.config.from_object(config_) # Cargar la configuración
    jwt = JWTManager(app) # Crea la instancia de JWTManager

    # Inicializa la base de datos
    db.init_app(app)


    app.register_blueprint(bp_route_home)
    app.register_blueprint(bp_route_taxis)
    app.register_blueprint(bp_route_trajectories)
    app.register_blueprint(bp_route_latest)
    app.register_blueprint(bp_route_user)
    app.register_blueprint(bp_route_login)


    # Manejan los errores en el proceso de autenticación

    #callback: es proporcionado por la propia extensión. y es obligatorio pasarlo
    #como argumento en la función para que el decorador funcione correctamente
    @jwt.unauthorized_loader
    def response_unauthorized(callback):
        return jsonify({'error': 'El token no existe'}), 401

    #jwt_header contiene los datos del encabezado, como el algoritmo de firma y el tipo de token
    #jwt_payload contiene la información del usuario y otros datos
    @jwt.expired_token_loader
    def response_token_expired(jwt_header, jwt_payload):
        return jsonify({'error': 'El token ha expirado'}), 401

    @jwt.invalid_token_loader
    def response_token_invalid(callback):
        return jsonify({'error': 'El token es invalido'}), 401



    # Registra los modelos
    with app.app_context() :
        db.create_all()          # Crea las tablas en la base de datos
        return app
