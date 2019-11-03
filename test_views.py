import requests


def test_result():
    """

    :return:
    """
    response = requests.get('http://127.0.0.1:5000/result/', params={'query': 'dakar'},)

    assert response.status_code == 200
    assert response.json()['lat'] == 14.716677
    assert response.json()['lng'] == -17.4676861
    assert response.json()['address'] == 'Dakar, Senegal'
