import pytest

def test_create_user(test_app, client):

    data = {
        'name': 'Thiago Silva', 
        'email': 'ThiagoSV05@test.com', 
        'password': 'SilThiagoVa' 
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




def test_update_user(test_app, client, create_user):

    update_data = {
        'name': 'Isabel Nunes'
    }

    uid = create_user
    response = client.patch(f'/users/{uid}', json=update_data)

    assert response.status_code == 200

    response_data = response.get_json()

    assert response_data['name'] == update_data['name']



def test_get_users_before_delete(test_app, client):

    params = {'page': 1, 'limit': 5 }
    response = client.get('/users', query_string=params)

    assert response.status_code == 200

    response_data = response.get_json()
    print('cantidad de users en db', len(response_data))
    assert len(response_data) == 2


def test_delete_user(test_app, client, create_user):

    uid = create_user

    response = client.delete(f'/users/{uid}')

    response_data = response.get_json()

    assert response.status_code == 200
    print(response_data['name'])
    assert response_data['name'] == "Nombre eliminado"


def test_get_users_after_delete(test_app, client):

    params = {'page': 1, 'limit': 5 }
    response = client.get('/users', query_string=params)

    assert response.status_code == 200

    response_data = response.get_json()
    
    print('cantidad de users en db', len(response_data))
    assert len(response_data) == 1