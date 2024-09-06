# Este file inicializa la aplicación Flask
from flask import Flask
from app.database.db import db
from app.routes.routes_taxis import bp_route_taxis
from app.routes.routes_home import bp_route_home

def create_app() :
    app = Flask(__name__)
    app.config.from_object('config.Config') # Cargar la configuración

    # Inicializa la base de datos
    db.init_app(app)

    app.register_blueprint(bp_route_home)

    app.register_blueprint(bp_route_taxis)

    # Registra los modelos
    with app.app_context() :
        db.create_all()          # Crea las tablas en la base de datos
        return app

