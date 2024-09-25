from app import db

class Taxi(db.Model):
    """"
    Representa la tabla 'taxis' en la base de datos
 
    args: 
        id (int): Número id único para cada taxi.
        plate(str): Placa del taxi, máximo tiene 10 caracteres

    método:
        to_dict(): convierte la data en un diccionario

    """
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(10))

    def to_dict(self):
        return {
        "id": self.id,
        "plate": self.plate
        }