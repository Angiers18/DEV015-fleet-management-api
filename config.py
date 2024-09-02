# Este archivo configura la app
import os # os interactua con el sistema operativo

# Configura la cadena de conexión desde el panel de Vercel
class Config:

    SQLALCHEMY_DATABASE_URI = (
         "postgresql://default:ARgfMHVes85Z@ep-white-morning-a40680zk.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
    )
    #no rastrear todas las modificaciones SQL, eso hace que la aplicación sea más eficiente.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
