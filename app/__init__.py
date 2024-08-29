# Este file inicializa la aplicación Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializar SQLAlchemy 
db = SQLAlchemy()


def create_app():
   app = Flask(__name__)
   app.config.from_pyfile('config.py') # Cargar la configuración

# Inicializa la base de datos con la aplicación
   db.init_app(app)

# Registra los modelos
   with app.app_context():
        from app import models        # Importa los modelos directamente
        db.create_all() # Crea las tablas en la base de datos

   return app




