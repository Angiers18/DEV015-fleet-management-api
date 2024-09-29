from flask import jsonify
from app.routes.routes_users import create_new_user


def test_create_user(test_app, client):

    data = {

        'name': 'Aurora Nunes', 
        'email': 'AuroNun17@test.com', 
        'password': 'Nun3sAur01' 
    } # data de prueba para ingresar en db

    # simula peticion de cliente
    response = client.post('/users', json=data)

    assert response.status_code == 201

    #obtiene la respuesta generada
    response_data = response.get_json()

    assert response_data['name'] == data['name']
    assert response_data['email'] == data['email']

    # retorna el ID del usuario creado
    print('Nuevo ID creado', response_data['id'])
    return response_data['id']
