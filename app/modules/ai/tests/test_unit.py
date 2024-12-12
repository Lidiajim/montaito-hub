import unittest
from unittest.mock import MagicMock, patch
from google.cloud import dialogflow_v2 as dialogflow
from app.modules.ai.services import AiService  # Ajusta el import según tu estructura
from google.api_core.exceptions import GoogleAPICallError


class TestAiService(unittest.TestCase):

    @patch("app.modules.ai.services.dialogflow.SessionsClient")
    def test_detect_intent_texts(self, MockSessionsClient):
        """Prueba el caso normal donde se obtiene una respuesta válida."""
        mock_session_client = MockSessionsClient.return_value
        mock_session_path = "projects/test-project-id/agent/sessions/test-session-id"
        mock_session_client.session_path.return_value = mock_session_path

        mock_query_result = MagicMock()
        mock_query_result.fulfillment_text = "Respuesta simulada del agente"
        
        mock_response = MagicMock()
        mock_response.query_result = mock_query_result
        
        mock_session_client.detect_intent.return_value = mock_response

        ai_service = AiService()
        response = ai_service.detect_intent_texts(
            project_id="test-project-id",
            session_id="test-session-id",
            text="Hola, ¿cómo estás?",
            language_code="es"
        )

        self.assertEqual(response, "Respuesta simulada del agente")

    @patch("app.modules.ai.services.dialogflow.SessionsClient")
    def test_detect_intent_texts_empty_response(self, MockSessionsClient):
        """Prueba el caso donde fulfillment_text está vacío."""
        mock_session_client = MockSessionsClient.return_value
        mock_session_path = "projects/test-project-id/agent/sessions/test-session-id"
        mock_session_client.session_path.return_value = mock_session_path

        mock_query_result = MagicMock()
        mock_query_result.fulfillment_text = ""  # Simula una respuesta vacía

        mock_response = MagicMock()
        mock_response.query_result = mock_query_result

        mock_session_client.detect_intent.return_value = mock_response

        ai_service = AiService()
        response = ai_service.detect_intent_texts(
            project_id="test-project-id",
            session_id="test-session-id",
            text="Hola, ¿cómo estás?",
            language_code="es"
        )

        self.assertEqual(response, "")  # Espera una cadena vacía como respuesta

    @patch("app.modules.ai.services.dialogflow.SessionsClient")
    def test_detect_intent_texts_with_exception(self, MockSessionsClient):
        """Prueba el manejo de excepciones cuando detect_intent falla."""
        mock_session_client = MockSessionsClient.return_value
        mock_session_path = "projects/test-project-id/agent/sessions/test-session-id"
        mock_session_client.session_path.return_value = mock_session_path

        # Simula que detect_intent lanza una excepción
        mock_session_client.detect_intent.side_effect = GoogleAPICallError("Error en Dialogflow")

        ai_service = AiService()
        with self.assertRaises(GoogleAPICallError):
            ai_service.detect_intent_texts(
                project_id="test-project-id",
                session_id="test-session-id",
                text="Hola, ¿cómo estás?",
                language_code="es"
            )

    @patch("app.modules.ai.services.dialogflow.SessionsClient")
    def test_detect_intent_texts_language_code_validation(self, MockSessionsClient):
        """Prueba el comportamiento con un language_code inválido."""
        mock_session_client = MockSessionsClient.return_value
        mock_session_path = "projects/test-project-id/agent/sessions/test-session-id"
        mock_session_client.session_path.return_value = mock_session_path

        mock_query_result = MagicMock()
        mock_query_result.fulfillment_text = "Respuesta simulada del agente"
        
        mock_response = MagicMock()
        mock_response.query_result = mock_query_result
        
        mock_session_client.detect_intent.return_value = mock_response

        ai_service = AiService()
        response = ai_service.detect_intent_texts(
            project_id="test-project-id",
            session_id="test-session-id",
            text="Hola, ¿cómo estás?",
            language_code="invalid-language-code"  # Código de idioma incorrecto
        )

        self.assertEqual(response, "Respuesta simulada del agente")  # Solo verifica que no haya error


if __name__ == "__main__":
    unittest.main()
