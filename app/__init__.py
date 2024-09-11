# Este file inicializa la aplicación Flask
from flask import Flask
from app.database.db import db
from app.routes.routes_taxis import bp_route_taxis
from app.routes.routes_home import bp_route_home
from app.routes.routes_trajectories import bp_route_trajectories
from app.routes.routes_latest import bp_route_latest


def create_app() :
    app = Flask(__name__)
    app.config.from_object('config.Config') # Cargar la configuración

    # Inicializa la base de datos
    db.init_app(app)

    app.register_blueprint(bp_route_home)

    app.register_blueprint(bp_route_taxis)

    bp_route_trajectories.register_blueprint(bp_route_latest)
    app.register_blueprint(bp_route_trajectories)
    

    # Registra los modelos
    with app.app_context() :
        db.create_all()          # Crea las tablas en la base de datos
        return app

