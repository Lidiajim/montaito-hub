import pytest

def test_fakenodo_response_keys(test_client, example_json):
    """
    Prueba que la respuesta contiene todas las claves esperadas en el JSON.
    """
    response = test_client.get('/fakenodo/deposit/depositions')
    assert response.status_code == 200, "El código de estado no es 200"

    response_data = response.get_json()

    # Verificar claves principales en la respuesta
    expected_keys = {"id", "access", "created", "files", "metadata", "status", "updated"}
    assert expected_keys.issubset(response_data.keys()), "Faltan claves principales en el JSON de respuesta"


def test_fakenodo_metadata_keys(test_client, example_json):
    """
    Prueba que la sección 'metadata' en la respuesta contiene las claves esperadas.
    """
    response = test_client.get('/fakenodo/deposit/depositions')
    assert response.status_code == 200, "El código de estado no es 200"

    response_data = response.get_json()
    metadata = response_data.get("metadata", {})

    expected_metadata_keys = {"title", "publisher", "resource_type", "rights", "creators", "publication_date"}
    assert expected_metadata_keys.issubset(metadata.keys()), "Faltan claves en la sección 'metadata'"


def test_fakenodo_file_entries(test_client, example_json):
    """
    Verifica la existencia y estructura de archivos en la respuesta.
    """
    response = test_client.get('/fakenodo/deposit/depositions')
    assert response.status_code == 200, "El código de estado no es 200"

    response_data = response.get_json()
    files = response_data.get("files", {}).get("entries", {})

    assert isinstance(files, dict), "La sección 'entries' no es un diccionario"
    assert "file1.uvl" in files, "El archivo 'file1.uvl' no está presente en 'entries'"

    file1 = files["file1.uvl"]
    assert file1["checksum"] == example_json["files"]["entries"]["file1.uvl"]["checksum"], "El checksum del archivo no coincide"
    assert file1["size"] == example_json["files"]["entries"]["file1.uvl"]["size"], "El tamaño del archivo no coincide"


def test_fakenodo_access_structure(test_client, example_json):
    """
    Verifica la estructura de la sección 'access' en la respuesta.
    """
    response = test_client.get('/fakenodo/deposit/depositions')
    assert response.status_code == 200, "El código de estado no es 200"

    response_data = response.get_json()
    access = response_data.get("access", {})

    assert "files" in access, "La clave 'files' falta en 'access'"
    assert "record" in access, "La clave 'record' falta en 'access'"
    assert "status" in access, "La clave 'status' falta en 'access'"

    assert access["files"] == example_json["access"]["files"], "El valor de 'files' en 'access' no coincide"
    assert access["status"] == example_json["access"]["status"], "El valor de 'status' en 'access' no coincide"


def test_fakenodo_invalid_endpoint(test_client):
    """
    Prueba un endpoint inexistente para verificar que devuelve 404.
    """
    response = test_client.get('/fakenodo/deposit/invalid_endpoint')
    assert response.status_code == 404, "El endpoint inválido no devuelve 404"
