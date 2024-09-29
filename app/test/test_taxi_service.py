from app.services.taxi_service import query_taxis


def test_query_taxis(mock_db_session):

    result = query_taxis(page=1, per_page=10, plate='S1', limit=5)
    print("Resultado de la consulta:", result)
    assert len(result) == 1
    assert result[0]['plate'] == 'ARS181'
