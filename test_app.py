import pytest
from main import app

@pytest.fixture
def client():
    """Cria um cliente de teste para o Flask."""
    with app.test_client() as client:
        yield client

def test_main_route(client):
    """Testa a rota principal ('/') para verificar o título da página."""
    response = client.get("/")
    assert response.status_code == 200  # Verifica se o status é 200 OK
    assert b"Hello DevOps Fans V2." in response.data  # Valida o conteúdo da resposta

def test_template_render(client):
    """Verifica se o template foi renderizado corretamente."""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<h1>Hello DevOps Fans V2.</h1>' in response.data  # Verifica o HTML específico

def test_invalid_route(client):
    """Testa uma rota inexistente para garantir que retorna 404."""
    response = client.get("/invalid")
    assert response.status_code == 404
