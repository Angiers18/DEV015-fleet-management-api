# Este file inicializa la aplicación Flask
from flask import Flask, jsonify
from app.db import db
from app.models import Taxi

def create_app() :
    app = Flask(__name__)
    app.config.from_object('config.Config') # Cargar la configuración

    # Inicializa la base de datos
    db.init_app(app)


    @app.route("/")
    def hi() :
            return "Hola mundo!!"


    @app.route("/taxi", methods=['GET'])
    def get_taxis() :
       # Consulta los taxis en la bade de datos
       taxi = Taxi.query.all()
       # Los vuelve los lista de diccionarios
       taxi_list = [{"id": taxi.id, "plate": taxi.plate} for taxi in taxi]

       return jsonify(taxi_list)
         
    @app.route("/angie")
    def hola():
       return "Estamos Bien!!"

         # Registra los modelos
    with app.app_context() :
      db.create_all()          # Crea las tablas en la base de datos
      return app






