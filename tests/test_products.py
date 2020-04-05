from services.products.models import Product
from services.products.respositories import ProductRepository


def test_get_products_returns_list_of_products(client, mocker):
    given_products = [
        Product('uuid-1', 'test-name-1'),
        Product('uuid-2', 'test-name-2'),
    ]
    mocker.patch.object(ProductRepository, 'list').return_value = given_products
    given_url = '/products/'
    expected_response_status_code = 200
    expected_response_json = [
        {'uuid': 'uuid-1', 'name': 'test-name-1',},
        {'uuid': 'uuid-2', 'name': 'test-name-2',},
    ]

    response = client.get(given_url)

    assert response.status_code == expected_response_status_code
    assert response.json == expected_response_json
