import pytest
from flask import jsonify


@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extiende la fixture test_client para añadir datos específicos en el contexto de pruebas del módulo.
    """
    with test_client.application.app_context():
        # Configuración específica del contexto de pruebas si fuera necesario
        pass

    yield test_client

@pytest.fixture
def example_json():
    """Proporciona el JSON de ejemplo similar al que compartirá el endpoint"""
    return {
        "access": {
            "embargo": {"active": False, "reason": None},
            "files": "restricted",
            "record": "public",
            "status": "restricted"
        },
        "created": "2024-11-12T20:33:29.945089+00:00",
        "custom_fields": {},
        "deletion_status": {"is_deleted": False, "status": "P"},
        "files": {
            "count": 1,
            "enabled": True,
            "entries": {
                "file1.uvl": {
                    "access": {"hidden": False},
                    "checksum": "md5:c80ca2ca9edec3c8b001e42922229d4c",
                    "ext": "uvl",
                    "id": "b9a8cf2a-c1bd-4f08-9afc-d9029cf6a485",
                    "key": "file1.uvl",
                    "links": {
                        "content": "https://zenodo.org/api/records/14110637/files/file1.uvl/content",
                        "self": "https://zenodo.org/api/records/14110637/files/file1.uvl"
                    },
                    "metadata": {},
                    "mimetype": "application/octet-stream",
                    "size": 414,
                    "storage_class": "L"
                }
            },
            "order": [],
            "total_bytes": 414
        },
        "id": "14110637",
        "is_draft": False,
        "is_published": True,
        "metadata": {
            "creators": [{"person_or_org": {"family_name": "junyao", "name": "junyao", "type": "personal"}}],
            "dates": [
                {
                    "date": "2024-11-12",
                    "description": "date",
                    "type": {"id": "accepted", "title": {"de": "Angenommen", "en": "Accepted"}}
                }
            ],
            "description": "<p>For testing unit.</p>",
            "languages": [{"id": "spa", "title": {"en": "Spanish"}}],
            "publication_date": "2024-11-12",
            "publisher": "Zenodo",
            "resource_type": {"id": "dataset", "title": {"de": "Datensatz", "en": "Dataset"}},
            "rights": [
                {
                    "description": {
                        "en": "The Creative Commons Attribution license allows re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited."
                    },
                    "icon": "cc-by-icon",
                    "id": "cc-by-4.0",
                    "props": {"scheme": "spdx", "url": "https://creativecommons.org/licenses/by/4.0/legalcode"},
                    "title": {"en": "Creative Commons Attribution 4.0 International"}
                }
            ],
            "title": "test_unit"
        },
        "status": "published",
        "updated": "2024-11-12T20:33:30.113813+00:00"
    }

def test_fakenodo_record_structure(test_client, example_json):
    """
    Prueba que el endpoint de fakenodo devuelve el JSON esperado y verifica algunas de sus claves y valores.
    """
    response = test_client.get('/fakenodo/deposit/depositions')  # Ajusta la ruta del endpoint según tu aplicación
    assert response.status_code == 200, "El código de estado no es 200 como se esperaba"
    
    # Obtenemos el JSON de la respuesta
    response_data = response.get_json()

    # Verificamos algunas claves principales y sus valores
    assert response_data["id"] == example_json["id"], "El ID no coincide con el esperado"
    assert response_data["access"]["status"] == example_json["access"]["status"], "El estado de acceso no coincide"
    assert response_data["files"]["count"] == example_json["files"]["count"], "La cantidad de archivos no coincide"
    assert response_data["metadata"]["title"] == example_json["metadata"]["title"], "El título en metadata no coincide"
    assert response_data["metadata"]["publisher"] == example_json["metadata"]["publisher"], "El editor no coincide"
    assert response_data["metadata"]["rights"][0]["id"] == example_json["metadata"]["rights"][0]["id"], "El ID de derechos no coincide"
    assert response_data["status"] == example_json["status"], "El estado de publicación no coincide"

# Prueba de creación de registro (POST)

def test_create_fakenodo(test_client):
    """Prueba que se pueda crear un nuevo registro con POST"""
    payload = {
        "files": [{"name": "testfile.txt", "checksum": "md5:abc123"}]
    }

    response = test_client.post(
        '/fakenodo/deposit/depositions',
        json=payload
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Deposition created"
    assert "id" in data


# Prueba de eliminación de registro (DELETE)

def test_delete_fakenodo(test_client):
    """Prueba que se pueda eliminar un registro existente"""
    # Primero crea un registro
    payload = {"title": "To Delete", "description": "This record will be deleted"}
    create_response = test_client.post('/fakenodo/deposit/depositions', json=payload)
    record_id = create_response.get_json()["id"]

    # Ahora elimina el registro
    response = test_client.delete(f'/fakenodo/deposit/depositions/{record_id}')
    assert response.status_code == 200
    assert response.get_json()["message"] == f"Deposition {record_id} deleted"

    # Verifica que el registro ya no existe
    response_not_found = test_client.get(f'/fakenodo/deposit/depositions/{record_id}')
    assert response_not_found.status_code == 405


# Prueba de estructura de archivos

def test_file_structure_in_response(test_client, example_json):
    """Prueba que la estructura de archivos dentro del JSON sea correcta"""
    response = test_client.get('/fakenodo/deposit/depositions')
    assert response.status_code == 200

    response_data = response.get_json()
    files = response_data["files"]["entries"]

    # Verifica que los archivos tengan las claves esperadas
    for file_key, file_data in files.items():
        assert "checksum" in file_data, "Falta el checksum en el archivo"
        assert "links" in file_data, "Faltan los links en el archivo"
        assert "size" in file_data, "Falta el tamaño del archivo"