from flask import url_for


def test_hello_world_returns_valid_payload(client):
    expected_response_status_code = 200
    expected_response_json = {'hello': 'world'}

    actual_response = client.get(url_for('helloworld'))

    assert actual_response.status_code == expected_response_status_code
    assert actual_response.json == expected_response_json
