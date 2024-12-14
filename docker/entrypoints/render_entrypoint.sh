#!/bin/bash

# ---------------------------------------------------------------------------
# Creative Commons CC BY 4.0 - David Romero - Diverso Lab
# ---------------------------------------------------------------------------

# Exit immediately if a command exits with a non-zero status
set -e

# Verificar si el token de Discord está disponible
if [ -z "$DISCORD_BOT_TOKEN" ]; then
    echo "Error: DISCORD_BOT_TOKEN no está configurado."
    exit 1
fi

echo "Token de Discord configurado correctamente."

# Initialize migrations only if the migrations directory doesn't exist
if [ ! -d "migrations/versions" ]; then
    flask db init
    flask db migrate
fi

# Check if the database is empty
if [ $(mariadb -u $MARIADB_USER -p$MARIADB_PASSWORD -h $MARIADB_HOSTNAME -P $MARIADB_PORT -D $MARIADB_DATABASE -sse "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '$MARIADB_DATABASE';") -eq 0 ]; then
    echo "Empty database, migrating..."
    flask db upgrade
else
    echo "Database already initialized, updating migrations..."
    flask db upgrade
fi

# Iniciar el bot de Discord junto con la aplicación
echo "Iniciando el bot de Discord y la aplicación..."
python -m app.discord_bot &

# Start the application using Gunicorn
exec gunicorn --bind 0.0.0.0:80 app:app --log-level info --timeout 3600
