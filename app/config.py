"""
    Este archivo define las configuraciones de la app Flask

    Attributes:
    Config (class): Clase base que define la configuración de la base de datos de la aplicación.
    Test_Config(Config) (class): Clase que define la configuración de la base de datos para tests.

"""
from datetime import timedelta
import os # os interactua con el sistema operativo
from dotenv import load_dotenv

load_dotenv()

# Importa la variable de entorno(privada) desde el archivo .env
uri = os.getenv('BD_URI')
uri_test = os.getenv('BD_URI_TEST')
key = os.getenv('JWT_SECRET')

class Config:

    """
    Esta clase define los parámetros de configuración generales que son comunes a todos los
    entornos, como la configuración de la base de datos.

    SQLALCHEMY_DATABASE_URI (str): URI de la base de datos utilizada por SQLAlchemy.
    SQLALCHEMY_TRACK_MODIFICATIONS (bool): Deshabilita la notificación de cambios de SQLAlchemy.
    
    """
    SQLALCHEMY_DATABASE_URI = uri
    #no rastrear todas las modificaciones SQL, eso hace que la aplicación sea más eficiente.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #JWT captura la clave secreta del env
    SECRET_KEY = key
    #tiempo de expiracion del token
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class Test_Config(Config):

    SQLALCHEMY_DATABASE_URI = uri_test
    TESTING = True # Activa el modo de prueba
