from app import db

class User(db.Model):

    """"
     Representa la tabla 'users' en la base de datos.
    
     args: 
        id (int): Número ID unico para cada usuario.
        name (str): Nombre del usuario.
        email (str): Email del usuario.
        password (str): Contraseña del usuario.

     metodo:
        to_dict(): Convierte la data en un diccionario.

    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "email": self.email,
        "password": self.password
        }