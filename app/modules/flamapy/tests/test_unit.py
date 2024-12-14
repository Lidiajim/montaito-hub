from unittest.mock import MagicMock, patch
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
    

def test_to_splot_endpoint(test_client):
    """
    Test the /flamapy/to_splot/<int:file_id> endpoint.
    """
    with patch('app.modules.hubfile.services.HubfileService.get_by_id') as mock_get_by_id:
        mock_hubfile = MagicMock()
        mock_hubfile.get_path.return_value = '/mock/path/to/file.uvl'
        mock_hubfile.name = 'mock_file'
        mock_get_by_id.return_value = mock_hubfile

        with patch(
            'flamapy.metamodels.fm_metamodel.transformations.UVLReader.transform'
        ) as mock_transform, patch(
            'flamapy.metamodels.fm_metamodel.transformations.SPLOTWriter.transform'
        ) as mock_writer:
            mock_transform.return_value = MagicMock()
            mock_writer.return_value = None

            response = test_client.get(url_for('flamapy.to_splot', file_id=1))
            assert response.status_code == 200, "Unexpected status code"
            assert response.headers["Content-Disposition"].startswith("attachment")
            assert response.headers["Content-Type"] in ["application/octet-stream", "text/plain; charset=utf-8"]


def test_to_cnf_endpoint(test_client):
    """
    Test the /flamapy/to_cnf/<int:file_id> endpoint.
    """
    with patch('app.modules.hubfile.services.HubfileService.get_by_id') as mock_get_by_id:
        mock_hubfile = MagicMock()
        mock_hubfile.get_path.return_value = '/mock/path/to/file.uvl'
        mock_hubfile.name = 'mock_file'
        mock_get_by_id.return_value = mock_hubfile

        with patch(
            'flamapy.metamodels.fm_metamodel.transformations.UVLReader.transform'
        ) as mock_transform, patch(
            'flamapy.metamodels.pysat_metamodel.transformations.FmToPysat.transform'
        ) as mock_pysat_transform, patch(
            'flamapy.metamodels.pysat_metamodel.transformations.DimacsWriter.transform'
        ) as mock_writer:
            mock_transform.return_value = MagicMock()
            mock_pysat_transform.return_value = MagicMock()
            mock_writer.return_value = None

            response = test_client.get(url_for('flamapy.to_cnf', file_id=1))
            assert response.status_code == 200, "Unexpected status code"
            assert response.headers["Content-Disposition"].startswith("attachment")
            assert response.headers["Content-Type"] in ["application/octet-stream", "text/plain; charset=utf-8"]
