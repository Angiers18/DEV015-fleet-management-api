"""
    Este modulo define los modelos de base de datos para una aplicacion que gestiona taxis y sus trayectorias.

    Clases:
        Taxi: Representa un taxi con su placa.
        Trajectory: Representa una trayectoria realizada por un taxi, con datos de ubicacion y fecha.

    Ambas clases incluyen metodos para convertir sus  atributos en formato diccionario (JSON).
"""

from app import db

class Taxi(db.Model):
    """"
    Representa la tabla 'taxis' en la base de datos.
    
    Atributos: 
        id (int): numero id unico por taxi.
        plate(str): placa del taxi, maximo tiene 10 caracteres.

    Metodo:
        to_dict(): convierte los atributos en un diccionario (JSON).

    """
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(10))

    def to_dict(self):
        return {
        "id": self.id,
        "plate": self.plate
        }

class Trajectory(db.Model):

    """"
     Representa la tabla 'trajectories' en la base de datos.
    
     Atributos: 
        id (int): numero id unico para cada trajectoria.
        taxi_id (int): numero id unico por taxi (relacionado con la tabla 'taxis).
        date (dateTime): fecha y hora de la trajectoria.
        latitude (float): latitud de la trayectoria.
        longitude (float) longitud de la trayectoria.

     Metodo:
        to_dict(): convierte los atributos en un diccionario (JSON).

    """

    __tablename__ = 'trajectories'

    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, db.ForeignKey('taxis.id'))
    date = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def to_dict(self):
        return {
        "id": self.id,
        "taxiId": self.taxi_id,
        "date": self.date,
        "latitude": self.latitude,
        "longitude": self.longitude
        }

