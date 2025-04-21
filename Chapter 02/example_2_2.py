import requests

def test_payment_processing():
    response = requests.post("http://api.example.com/payments/process", json={"amount": 100, "currency": "USD"})
    assert response.status_code == 200
    assert response.json()['status'] == 'success'
    assert 'transaction_id' in response.json()