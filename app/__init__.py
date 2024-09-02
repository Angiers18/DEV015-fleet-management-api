# Este file inicializa la aplicación Flask
from flask import Flask, request
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


    @app.route("/taxis", methods=['GET'])
    def get_taxis() :

        #paginacion
        page = int(request.args.get('page', 1)) #una pagina
        per_page = int(request.args.get('per_page', 10)) #diez elementos por pagina
        plate = request.args.get('plate', '') # queryparams

        query = db.session.query(Taxi) # inicia una consulta
        if plate:
         # like y % funcionan en sql verifica una secuencia de caracteres
            query = query.filter(Taxi.plate.like(f'%{plate}%'))

        # Obtiene total de resultados
        total = query.count()

        taxis = query.offset((page - 1) * per_page).limit(per_page).all()

        return {
            'page': page,
            'per_page': per_page,
            'total': total,
            'taxis': [taxi.to_dict() for taxi in taxis]
        }

    @app.route("/angie")
    def hola():
        return "Estamos Bien!!"

         # Registra los modelos
    with app.app_context() :
        db.create_all()          # Crea las tablas en la base de datos
        return app

