from services.orders.models import OrderModel
from services.orders.respositories import OrdersRepository


def test_get_returns_list_of_orders(client, given_products, mocker):
    given_orders = [
        OrderModel('order-uuid-1', given_products,),
        OrderModel('order-uuid-2', given_products,),
    ]
    mocker.patch.object(OrdersRepository, 'list').return_value = given_orders
    given_url = '/orders/'
    expected_response_status_code = 200
    expected_response_json = [
        {
            'products': [
                {'name': 'test-name-1', 'uuid': 'uuid-1'},
                {'name': 'test-name-2', 'uuid': 'uuid-2'},
            ],
            'uuid': 'order-uuid-1',
        },
        {
            'products': [
                {'name': 'test-name-1', 'uuid': 'uuid-1'},
                {'name': 'test-name-2', 'uuid': 'uuid-2'},
            ],
            'uuid': 'order-uuid-2',
        },
    ]

    response = client.get(given_url)

    assert response.status_code == expected_response_status_code
    assert response.json == expected_response_json


def test_get_returns_order_when_order_uuid_given(client, given_products, mocker):
    given_order = OrderModel('order-uuid-1', given_products)
    mocker.patch.object(OrdersRepository, 'get').return_value = given_order
    given_order_uuid = 'order-uuid-1'
    given_url = f'/orders/{given_order_uuid}'
    expected_response_status_code = 200
    expected_response_json = {
        'products': [
            {'name': 'test-name-1', 'uuid': 'uuid-1'},
            {'name': 'test-name-2', 'uuid': 'uuid-2'},
        ],
        'uuid': 'order-uuid-1',
    }

    response = client.get(given_url)

    assert response.status_code == expected_response_status_code
    assert response.json == expected_response_json


def test_post_creates_and_returns_new_order(client, given_products):
    given_payload = {
        'uuid': 'test-created-uuid',
        'products': [
            {'name': 'test-name-1', 'uuid': 'uuid-1'},
            {'name': 'test-name-2', 'uuid': 'uuid-2'},
        ],
    }
    given_url = '/orders/'
    expected_response_status_code = 201
    expected_response_json = {
        'products': [
            {'name': 'test-name-1', 'uuid': 'uuid-1'},
            {'name': 'test-name-2', 'uuid': 'uuid-2'},
        ],
        'uuid': 'test-created-uuid',
    }

    response = client.post(given_url, json=given_payload, content_type='application/json')

    assert response.status_code == expected_response_status_code
    assert response.json == expected_response_json


def test_put_updates_and_returns_order(client, given_products, mocker):
    given_order_uuid = 'order-uuid-1'
    given_order = OrderModel(given_order_uuid, given_products)
    mocker.patch.object(OrdersRepository, 'get').return_value = given_order
    given_payload = {
        'uuid': 'changed-test-created-uuid',
        'products': [
            {'name': 'test-name-1', 'uuid': 'uuid-1'},
            {'name': 'test-name-2', 'uuid': 'uuid-2'},
        ],
    }
    given_url = f'/orders/{given_order_uuid}'
    expected_response_status_code = 200
    expected_response_json = {
        'products': [
            {'name': 'test-name-1', 'uuid': 'uuid-1'},
            {'name': 'test-name-2', 'uuid': 'uuid-2'},
        ],
        'uuid': 'changed-test-created-uuid',
    }

    response = client.put(given_url, json=given_payload, content_type='application/json')

    assert response.status_code == expected_response_status_code
    assert response.json == expected_response_json


def test_delete_removes_existing_order(client, given_products, mocker):
    given_order_uuid = 'order-uuid-1'
    given_order = OrderModel(given_order_uuid, given_products)
    mocker.patch.object(OrdersRepository, 'get').return_value = given_order
    given_url = f'/orders/{given_order_uuid}'
    expected_response_status_code = 200
    expected_response_json = {
        'products': [
            {'name': 'test-name-1', 'uuid': 'uuid-1'},
            {'name': 'test-name-2', 'uuid': 'uuid-2'},
        ],
        'uuid': 'order-uuid-1',
    }

    response = client.delete(given_url)

    assert response.status_code == expected_response_status_code
    assert response.json == expected_response_json
