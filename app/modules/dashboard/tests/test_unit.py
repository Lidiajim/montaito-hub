import pytest
from unittest.mock import MagicMock
from app.modules.dashboard.repositories import DashboardRepository
from app import db


@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extiende la fixture test_client para añadir datos específicos para las pruebas de este módulo.
    """
    with test_client.application.app_context():
        # Si necesitas agregar datos iniciales a la base de datos para las pruebas, hazlo aquí.
        # db.session.add(<element>)
        # db.session.commit()
        pass

    yield test_client


def test_get_total_datasets(test_client):
    """
    Prueba para verificar que el método get_total_datasets funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    dashboard_repository.dataset_repository.count_synchronized_datasets = MagicMock(return_value=10)

    result = dashboard_repository.get_total_datasets()
    assert result == 10, f"Se esperaba 10, pero se obtuvo {result}"


def test_get_total_users(test_client):
    """
    Prueba para verificar que el método get_total_users funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    db.session.query = MagicMock(return_value=MagicMock(scalar=MagicMock(return_value=50)))

    result = dashboard_repository.get_total_users()
    assert result == 50, f"Se esperaba 50, pero se obtuvo {result}"


def test_get_total_views(test_client):
    """
    Prueba para verificar que el método get_total_views funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    dashboard_repository.ds_view_record_repository.total_dataset_views = MagicMock(return_value=200)

    result = dashboard_repository.get_total_views()
    assert result == 200, f"Se esperaba 200, pero se obtuvo {result}"


def test_get_total_downloads(test_client):
    """
    Prueba para verificar que el método get_total_downloads funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    dashboard_repository.ds_download_record_repository.total_dataset_downloads = MagicMock(return_value=300)

    result = dashboard_repository.get_total_downloads()
    assert result == 300, f"Se esperaba 300, pero se obtuvo {result}"


def test_get_average_dataset_rating(test_client):
    """
    Prueba para verificar que el método get_average_dataset_rating funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    db.session.query = MagicMock(return_value=MagicMock(scalar=MagicMock(return_value=4.5)))

    result = dashboard_repository.get_average_dataset_rating()
    assert result == 4.5, f"Se esperaba 4.5, pero se obtuvo {result}"


def test_get_total_datasets_by_user_id(test_client):
    """
    Prueba para verificar que el método get_total_datasets_by_user_id funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    db.session.query = MagicMock(return_value=MagicMock(filter=MagicMock(return_value=MagicMock(count=MagicMock(return_value=5)))))

    result = dashboard_repository.get_total_datasets_by_user_id(user_id=1)
    assert result == 5, f"Se esperaba 5, pero se obtuvo {result}"


def test_get_average_dataset_rating_by_user_id(test_client):
    """
    Prueba para verificar que el método get_average_dataset_rating_by_user_id funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    db.session.query = MagicMock(return_value=MagicMock(join=MagicMock(return_value=MagicMock(filter=MagicMock(return_value=MagicMock(scalar=MagicMock(return_value=4.2)))))))

    result = dashboard_repository.get_average_dataset_rating_by_user_id(user_id=1)
    assert result == 4.2, f"Se esperaba 4.2, pero se obtuvo {result}"


def test_get_total_views_by_user_id(test_client):
    """
    Prueba para verificar que el método get_total_views_by_user_id funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    db.session.query = MagicMock(return_value=MagicMock(join=MagicMock(return_value=MagicMock(filter=MagicMock(return_value=MagicMock(scalar=MagicMock(return_value=15)))))))

    result = dashboard_repository.get_total_views_by_user_id(user_id=1)
    assert result == 15, f"Se esperaba 15, pero se obtuvo {result}"


def test_get_total_downloads_by_user_id(test_client):
    """
    Prueba para verificar que el método get_total_downloads_by_user_id funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    dashboard_repository.ds_download_record_repository.total_dataset_downloads_by_user_id = MagicMock(return_value=8)

    result = dashboard_repository.get_total_downloads_by_user_id(user_id=1)
    assert result == 8, f"Se esperaba 8, pero se obtuvo {result}"


def test_get_total_feature_models_by_user_id(test_client):
    """
    Prueba para verificar que el método get_total_feature_models_by_user_id funciona correctamente.
    """
    dashboard_repository = DashboardRepository()
    dashboard_repository.feature_model_repository.count_feature_models_by_user_id = MagicMock(return_value=12)

    result = dashboard_repository.get_total_feature_models_by_user_id(user_id=1)
    assert result == 12, f"Se esperaba 12, pero se obtuvo {result}"
