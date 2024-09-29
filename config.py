"""
    Este archivo define las configuraciones de la app Flask

    Attributes:
    Config (class): Clase base que define la configuración de la base de datos de la aplicación.
    Test_Config(Config) (class): Clase que define la configuración de la base de datos para tests.

"""
import os # os interactua con el sistema operativo
from dotenv import load_dotenv

load_dotenv()

# Importa la variable de entorno(privada) desde el archivo .env
uri = os.getenv('BD_URI')

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
