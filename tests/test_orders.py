from services.orders.models import OrderModel
from services.orders.respositories import OrdersRepository


def test_orders_returns_list_of_orders(client, given_products, mocker):
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
