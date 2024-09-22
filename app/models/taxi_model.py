from app import db

class Taxi(db.Model):
    """"
    representa la tabla 'taxis' en la base de datos
    
    args: 
        id (int): numero id unico por taxi.
        plate(str): placa del taxi, maximo tiene 10 caracteres

    metodo:
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