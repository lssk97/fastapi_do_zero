from fastapi.testclient import TestClient
from src.main import app
import pytest

@pytest.fixture
def client():
    '''Fixture de testes do FastAPI'''
    return TestClient(app)

def test_read_main(client):
    '''Teste de resposta do main router.'''
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message' : 'hello world'}
