from app import db

class Trajectory(db.Model):

    """"
     Representa la tabla 'trajectories' en la base de datos
    
     args: 
        id (int): Número ID único para cada trayectoria
        taxi_id (int): Número ID único por taxi (relacionado con la tabla 'taxis')
        date (dateTime): fecha y hora de la trayectoria
        latitude (float): latitud de la trayectoria
        longitude (float) longitud de la trayectoria

     método:
        to_dict(): Convierte la data en un diccionario

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
