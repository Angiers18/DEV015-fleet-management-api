from app import db

class User(db.Model):

    """"
     representa la tabla 'users' en la base de datos.
    
     args: 
        id (int): numero id unico para cada usuario.
        name (str): nombre del usuario.
        email (str): email del usuario.
        password (str): contraseña del usuario.

     metodo:
        to_dict(): convierte la data en un diccionario.

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