import unittest
from unittest.mock import MagicMock, patch
from google.cloud import dialogflow_v2 as dialogflow
from app.modules.ai.services import AiService  # Ajusta el import según tu estructura


class TestAiService(unittest.TestCase):

    @patch("app.modules.ai.services.dialogflow.SessionsClient")
    def test_detect_intent_texts(self, MockSessionsClient):
        # Crear una instancia simulada de SessionsClient
        mock_session_client = MockSessionsClient.return_value
        
        # Configurar un retorno simulado para detect_intent
        mock_session_path = "projects/test-project-id/agent/sessions/test-session-id"
        mock_session_client.session_path.return_value = mock_session_path
        
        mock_query_result = MagicMock()
        mock_query_result.fulfillment_text = "Respuesta simulada del agente"
        
        mock_response = MagicMock()
        mock_response.query_result = mock_query_result
        
        mock_session_client.detect_intent.return_value = mock_response
        
        # Crear instancia del servicio AI
        ai_service = AiService()
        
        # Parámetros de prueba
        project_id = "test-project-id"
        session_id = "test-session-id"
        user_message = "Hola, ¿cómo estás?"
        language_code = "es"
        
        # Llamar al método a probar
        response = ai_service.detect_intent_texts(project_id, session_id, user_message, language_code)
        
        # Validar que la respuesta sea correcta
        self.assertEqual(response, "Respuesta simulada del agente")
        
        # Verificar que session_path fue llamado correctamente
        mock_session_client.session_path.assert_called_once_with(project_id, session_id)
        
        # Verificar que detect_intent fue llamado con los parámetros correctos
        mock_session_client.detect_intent.assert_called_once_with(request={
            "session": mock_session_path,
            "query_input": dialogflow.QueryInput(
                text=dialogflow.TextInput(text=user_message, language_code=language_code)
            )
        })


if __name__ == "__main__":
    unittest.main()
