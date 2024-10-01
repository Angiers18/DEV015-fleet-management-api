import pytest
from app.models.taxi_model import Taxi
from app import create_app
from app.config import Test_Config
from app.database.db import db


@pytest.fixture
def mock_db_session(mocker):

    taxi_mock = Taxi(id=25, plate='ARS181')
    query_mock = mocker.patch('app.database.db.db.session.query')
    query_mock.return_value.filter.return_value.offset.return_value.limit.return_value.all.return_value = [taxi_mock]
    return query_mock



@pytest.fixture(scope='session')
def test_app():

    app = create_app(Test_Config)

    with app.app_context():
        db.create_all()  # crea tablas en la db para test
        yield app  

        # limpia la db después de cada test
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())  # elimina registros de cada tabla
        db.session.commit() 
        db.session.remove() # cierra la sesión en db



@pytest.fixture(scope='session')
def client(test_app):
    return test_app.test_client()


@pytest.fixture(scope='session')
def create_user(test_app, client):

    data = {
        'name': 'Aurora Nunes', 
        'email': 'AuroNun17@test.com', 
        'password': 'Nun3sAur01' 
    } # data de prueba para ingresar en db

    # simula peticion de cliente
    response = client.post('/users', json=data)

    #obtiene la respuesta generada
    response_data = response.get_json()

    # retorna el ID del usuario creado
    print('Nuevo ID creado(fixture) ', response_data['id'])
    yield response_data['id']