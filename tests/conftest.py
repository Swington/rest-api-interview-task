import pytest

from factory import initialize_app
from services.products.models import ProductModel


@pytest.fixture
def app():
    app = initialize_app()

    yield app


@pytest.fixture
def client(app):
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


@pytest.fixture
def given_products():
    given_products = [
        ProductModel('uuid-1', 'test-name-1'),
        ProductModel('uuid-2', 'test-name-2'),
    ]
    return given_products