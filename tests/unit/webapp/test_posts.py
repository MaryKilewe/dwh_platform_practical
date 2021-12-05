from tests.unit.webapp import client
import json

def test_add_patients(client):

    mock_request_headers = {
        'authorization-sha256': '123'
    }

    mock_request_data = {
        'request_id': '123',
        'payload': {
            'first_name': 'pi',
            'last_name': 'script',
            'gender': 'Female',
            'age': 32,
            'facility': 'Nairobi Hospital',
            'county': 'Nairobi',
            'reg_date': '2021-08-24'
        }
    }

    response = client.post("/add_patients", data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 200

