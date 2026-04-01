#!/bin/sh
set -e

# Opcional: Esperar a que la DB esté lista (si usas Postgres)
if [ "$DB_USER" ]; then
    echo "Waiting for database..."
    # Intenta conectarse hasta que responda (necesitas instalar postgresql-client en el Dockerfile)
    # O un simple sleep para pruebas rápidas:
    sleep 5
fi

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Creación de superusuario (Tu lógica es correcta)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "Checking superuser..."
    python manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.getenv('DJANGO_SUPERUSER_USERNAME')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=os.getenv('DJANGO_SUPERUSER_EMAIL', ''),
        password=os.getenv('DJANGO_SUPERUSER_PASSWORD')
    )
    print(f'Superuser {username} created')
PY
fi

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3