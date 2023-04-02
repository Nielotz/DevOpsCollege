import requests

BASE_URL = "http://localhost:8000"

def test_api_mul():
    url = f"{BASE_URL}/api/mul?a=2&b=3"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_api_sub():
    url = f"{BASE_URL}/api/sub?a=10&b=3"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"result": 7}

def test_api_div():
    url = f"{BASE_URL}/api/div?a=10&b=5"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"result": 2}

    url = f"{BASE_URL}/api/div?a=10&b=0"
    response = requests.get(url)
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}
