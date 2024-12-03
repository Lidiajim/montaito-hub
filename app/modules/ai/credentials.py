from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Autenticación con una cuenta de servicio
credentials = service_account.Credentials.from_service_account_file(
    '/home/user/Desktop/uvlhub_practicas/montaito-hub/core/blueprints/dialogflow_credentials.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']  # Agrega el scope necesario
)

# Verifica si las credenciales están listas para usarse
if credentials.expired:
    credentials.refresh(Request())