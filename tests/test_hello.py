def test_hello_world_returns_valid_payload(client):
    given_url = '/hello/'
    expected_response_status_code = 200
    expected_response_json = {'hello': 'world'}

    response = client.get(given_url)

    assert response.status_code == expected_response_status_code
    assert response.json == expected_response_json
