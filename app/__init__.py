import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from core.configuration.configuration import get_app_version
from core.managers.module_manager import ModuleManager
from core.managers.config_manager import ConfigManager
from core.managers.error_handler_manager import ErrorHandlerManager
from core.managers.logging_manager import LoggingManager
from app.modules.bot.bot import bot
from threading import Thread

# Cargar las variables de entorno
load_dotenv()

# Instancias globales
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='development'):
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__)

    # Cargar configuración según el entorno
    config_manager = ConfigManager(app)
    config_manager.load_config(config_name=config_name)

    # Inicializar SQLAlchemy y Migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar módulos
    module_manager = ModuleManager(app)
    module_manager.register_modules()

    # Registrar Login Manager
    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        from app.modules.auth.models import User
        return User.query.get(int(user_id))

    # Configurar logging
    logging_manager = LoggingManager(app)
    logging_manager.setup_logging()

    # Manejar errores
    error_handler_manager = ErrorHandlerManager(app)
    error_handler_manager.register_error_handlers()

    # Variables disponibles en plantillas Jinja2
    @app.context_processor
    def inject_vars_into_jinja():
        return {
            'FLASK_APP_NAME': os.getenv('FLASK_APP_NAME'),
            'FLASK_ENV': os.getenv('FLASK_ENV'),
            'DOMAIN': os.getenv('DOMAIN', 'localhost'),
            'APP_VERSION': get_app_version()
        }

    # Iniciar el bot si no está en pruebas
    if os.getenv("FLASK_ENV") != "testing":
        token = os.getenv("DISCORD_BOT_TOKEN")
        if token:
            bot_thread = Thread(target=bot.run, args=(token,), daemon=True)
            bot_thread.start()
        else:
            print("Discord bot token not set.")

    return app


# Crear la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Configurar el puerto dinámico para evitar conflictos
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    try:
        app.run(host="127.0.0.1", port=port)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"El puerto {port} está en uso. Intentando iniciar en el puerto 5001...")
            app.run(host="127.0.0.1", port=5001)
