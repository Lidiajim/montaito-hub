import unittest
from unittest.mock import MagicMock, patch
from app.modules.featuremodel.services import FeatureModelService
from app.modules.featuremodel.models import FeatureModelRating


class TestFeatureModelService(unittest.TestCase):
    def setUp(self):
        self.service = FeatureModelService()
        self.service.hubfile_service = MagicMock()
        self.service.repository = MagicMock()

    def test_total_feature_model_views(self):
        self.service.hubfile_service.total_hubfile_views.return_value = 42
        views = self.service.total_feature_model_views()
        self.assertEqual(views, 42)
        self.service.hubfile_service.total_hubfile_views.assert_called_once()

    def test_total_feature_model_downloads(self):
        self.service.hubfile_service.total_hubfile_downloads.return_value = 10
        downloads = self.service.total_feature_model_downloads()
        self.assertEqual(downloads, 10)
        self.service.hubfile_service.total_hubfile_downloads.assert_called_once()

    def test_count_feature_models(self):
        self.service.repository.count_feature_models.return_value = 5
        count = self.service.count_feature_models()
        self.assertEqual(count, 5)
        self.service.repository.count_feature_models.assert_called_once()

    def test_rate_dataset_new_rating(self):
        with patch('app.modules.featuremodel.services.db.session') as mock_session:
            mock_session.query.return_value.filter_by.return_value.first.return_value = None
            mock_session.add = MagicMock()
            mock_session.commit = MagicMock()

            feature_model_id = 1
            user_id = 2
            rating = 4

            result = self.service.rate_dataset(feature_model_id, user_id, rating)

            self.assertIsInstance(result, FeatureModelRating)
            self.assertEqual(result.rating, rating)
            mock_session.add.assert_called_once()
            mock_session.commit.assert_called_once()

    def test_rate_dataset_update_existing_rating(self):
        with patch('app.modules.featuremodel.services.db.session') as mock_session:
            existing_rating = FeatureModelRating(
                feature_model_id=1, user_id=2, rating=3
            )
            mock_session.query.return_value.filter_by.return_value.first.return_value = existing_rating
            mock_session.commit = MagicMock()

            new_rating_value = 5

            result = self.service.rate_dataset(1, 2, new_rating_value)

            self.assertEqual(result, existing_rating)
            self.assertEqual(result.rating, new_rating_value)
            mock_session.commit.assert_called_once()

    def test_rate_dataset_invalid_rating(self):
        with self.assertRaises(ValueError, msg="La calificación debe estar entre 1 y 5"):
            self.service.rate_dataset(1, 2, 6)
        with self.assertRaises(ValueError, msg="La calificación debe estar entre 1 y 5"):
            self.service.rate_dataset(1, 2, 0)

    def test_get_average_rating(self):
        with patch('app.modules.featuremodel.services.db.session') as mock_session:
            mock_session.query.return_value.filter_by.return_value.scalar.return_value = 4.5

            avg_rating = self.service.get_average_rating(1)
            self.assertEqual(avg_rating, 4.5)

            mock_session.query.return_value.filter_by.return_value.scalar.return_value = None

            avg_rating = self.service.get_average_rating(1)
            self.assertEqual(avg_rating, 0.0)


if __name__ == "__main__":
    unittest.main()
