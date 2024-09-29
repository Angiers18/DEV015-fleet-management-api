import pytest
from app.models.taxi_model import Taxi


@pytest.fixture
def mock_db_session(mocker):

    taxi_mock = Taxi(id=25, plate='ARS181')

    query_mock = mocker.patch('app.database.db.db.session.query')

    query_mock.return_value.filter.return_value.offset.return_value.limit.return_value.all.return_value = [taxi_mock]

    return query_mock

