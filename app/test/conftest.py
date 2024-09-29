import pytest
from app.models.taxi_model import Taxi
from app import create_app
from config import Test_Config


@pytest.fixture
def mock_db_session(mocker):

    taxi_mock = Taxi(id=25, plate='ARS181')
    query_mock = mocker.patch('app.database.db.db.session.query')
    query_mock.return_value.filter.return_value.offset.return_value.limit.return_value.all.return_value = [taxi_mock]
    return query_mock



@pytest.fixture
def test_app():

    app = create_app()
    app.config.from_object(Test_Config)
    yield app

@pytest.fixture
def client(test_app):
    return test_app.test_client()

@pytest.fixture
def runner(test_app):
    return test_app.test_cli_runner()
