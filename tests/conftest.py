import pytest

from factory import initialize_app


@pytest.fixture
def app():
    app = initialize_app()

    yield app


@pytest.fixture
def client(app):
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client
