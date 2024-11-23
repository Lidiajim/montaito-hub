from flask.cli import FlaskGroup
from threading import Thread
from app import create_app
from app.modules.bot.bot import bot
import os

# Crear la app Flask
app = create_app()

# Crear el CLI para Flask
cli = FlaskGroup(create_app=create_app)

def run_flask():
    """
    Inicia el servidor Flask.
    """
    app.run(host="0.0.0.0", port=5000)

def run_discord():
    """
    Inicia el bot de Discord.
    """
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))

if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    discord_thread = Thread(target=run_discord)

    flask_thread.start()
    discord_thread.start()

    flask_thread.join()
    discord_thread.join()
