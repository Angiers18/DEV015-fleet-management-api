"""
Este modulo inicia la aplicacion Flask.

Funciones:
    create_app(): Crea y configura una instancia de la aplicacion Flask.

Uso:
    Si el modulo se ejecuta directamente, se iniciara el servidor de desarrollo Flask
    con el modo de depuracion activado.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
