import pytest
from flask import jsonify
import json

@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extiende la fixture test_client para añadir datos específicos en el contexto de pruebas del módulo.
    """
    with test_client.application.app_context():
        # Aquí podrías añadir datos adicionales a la base de datos si fuera necesario.
        # db.session.add(<elemento>) y db.session.commit() para guardar los datos.
        pass

    yield test_client

def test_get_fakenodo_data(test_client):
    """
    Prueba unitaria para el endpoint que simula la obtención de datos de fakenodo.
    """
    # Simula una solicitud GET al endpoint de fakenodo
    response = test_client.get('/fakenodo/deposit/depositions')
    
    # Asegura que el endpoint responde con un código de estado 200
    assert response.status_code == 200, "El código de estado no es 200 como se esperaba"
    
    # Carga el JSON de la respuesta
    response_data = response.get_json()
    
    # Comprueba que las claves principales están presentes en la respuesta JSON
    assert "id" in response_data, "La clave 'id' falta en el JSON de respuesta"
    assert "doi" in response_data, "La clave 'doi' falta en el JSON de respuesta"
    assert "metadata" in response_data, "La clave 'metadata' falta en el JSON de respuesta"
    
    # Comprueba algunos valores específicos dentro de la respuesta
    assert response_data["doi"] == "10.5072/zenodo.127564", "El valor del DOI no es el esperado"
    assert response_data["metadata"]["title"] == "Testing", "El título en metadata no coincide con el esperado"

def test_sample_assertion(test_client):
    """
    Prueba de muestra para verificar que el marco de pruebas funciona correctamente.
    """
    greeting = "Hello, World!"
    assert greeting == "Hello, World!", "El saludo no coincide con 'Hello, World!'"

    
