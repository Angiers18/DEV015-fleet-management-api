# Este file inicializa la aplicación Flask
from flask import Flask
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
    jwt = JWTManager(app)

    # Inicializa la base de datos
    db.init_app(app)

    app.register_blueprint(bp_route_home)
    app.register_blueprint(bp_route_taxis)
    app.register_blueprint(bp_route_trajectories)
    app.register_blueprint(bp_route_latest)
    app.register_blueprint(bp_route_user)
    app.register_blueprint(bp_route_login)

    # Registra los modelos
    with app.app_context() :
        db.create_all()          # Crea las tablas en la base de datos
        return app
