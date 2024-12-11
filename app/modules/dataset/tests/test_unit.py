import pytest
from app import db
from app.modules.conftest import login, logout
from unittest.mock import patch, MagicMock
from app.modules.dataset.services import DataSetService
from app.modules.dataset.models import DatasetRating


@pytest.fixture
def dataset_service():
    return DataSetService()


def test_view_profile_with_login(test_client):

    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/profile/2")
    assert response.status_code == 200, "The profile page could not be accessed."


def test_view_profile_without_login(test_client):
    response = test_client.get("/profile/2")
    assert response.status_code == 200, "The profile page could not be accessed."


def test_rate_dataset_valid_rating(dataset_service):
    with patch('app.modules.dataset.services.db.session') as mock_session:
        mock_session.query.return_value.filter_by.return_value.first.return_value = None
        mock_session.add = MagicMock()
        mock_session.commit = MagicMock()

        dataset_id = 1
        user_id = 1
        rating = 4

        result = dataset_service.rate_dataset(dataset_id, user_id, rating)

        assert isinstance(result, DatasetRating)
        assert result.rating == rating
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()


def test_rate_dataset_update_existing_rating(dataset_service):
    with patch('app.modules.dataset.services.db.session') as mock_session:
        mock_existing_rating = MagicMock(rating=3)
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_existing_rating
        mock_session.commit = MagicMock()

        dataset_id = 1
        user_id = 1
        new_rating = 5

        result = dataset_service.rate_dataset(dataset_id, user_id, new_rating)

        assert result == mock_existing_rating
        assert result.rating == new_rating
        mock_session.commit.assert_called_once()


def test_rate_dataset_invalid_rating(dataset_service):
    with pytest.raises(ValueError, match="La calificación debe estar entre 1 y 5"):
        dataset_service.rate_dataset(dataset_id=1, user_id=1, rating=6)


def test_get_average_rating(dataset_service):
    with patch('app.modules.dataset.services.db.session') as mock_session:
        mock_session.query.return_value.filter_by.return_value.scalar.return_value = 4.5

        dataset_id = 1
        avg_rating = dataset_service.get_average_rating(dataset_id)

        assert avg_rating == 4.5


def test_get_average_rating_no_ratings(dataset_service):
    with patch('app.modules.dataset.services.db.session') as mock_session:
        mock_session.query.return_value.filter_by.return_value.scalar.return_value = None

        dataset_id = 1
        avg_rating = dataset_service.get_average_rating(dataset_id)

        assert avg_rating == 0.0


def test_get_datasets_ordered_by_rating(dataset_service):
    with patch('app.modules.dataset.services.db.session') as mock_session:
        mock_dataset1 = MagicMock()
        mock_dataset1.id = 1
        mock_dataset1.name = 'Dataset 1'
        mock_dataset2 = MagicMock()
        mock_dataset2.id = 2
        mock_dataset2.name = 'Dataset 2'
        mock_session.\
            query.return_value.outerjoin.return_value.group_by.return_value.order_by.return_value.all.return_value = [
                (mock_dataset1, 4.5),
                (mock_dataset2, 3.8),
            ]

        datasets_with_ratings = dataset_service.get_datasets_ordered_by_rating()

        assert len(datasets_with_ratings) == 2
        assert datasets_with_ratings[0][0].name == 'Dataset 1'
        assert datasets_with_ratings[0][1] == 4.5
        assert datasets_with_ratings[1][0].name == 'Dataset 2'
        assert datasets_with_ratings[1][1] == 3.8
