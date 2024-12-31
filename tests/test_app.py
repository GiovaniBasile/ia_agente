from http import HTTPStatus

from fastapi.testclient import TestClient

from ia_agente.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange/Organiza o ambiente de testes

    response = client.get('/')  # Action/Executa a ação que será testada

    assert response.status_code == HTTPStatus.OK  # Assert/Verifica o resultado
    assert response.json() == {'message': 'Olá mundo!'}  # Assert
