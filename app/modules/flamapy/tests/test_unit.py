import pytest
from flask import url_for


@pytest.fixture(scope='module')
def test_client():
    """
    Creates a Flask test client and ensures proper app context management.
    """
    from app import create_app  # Adjust this import if necessary
    app = create_app()
    app.config['SERVER_NAME'] = 'localhost'  # Set SERVER_NAME for tests
    app.config['TESTING'] = True  # Enable testing mode

    with app.app_context():
        with app.test_client() as client:
            yield client


def test_valid_endpoint(test_client):
    """
    Test the /flamapy/valid/<int:file_id> endpoint.
    """
    response = test_client.get(url_for('flamapy.valid', file_id=1))
    assert response.status_code == 200, "Unexpected status code"
    assert response.json.get("success") is True
    assert response.json.get("file_id") == 1


