#!/bin/sh

# Termina el script si algún comando falla
set -e

echo "Aplicando migraciones de la base de datos..."
python manage.py migrate --noinput

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Creando superusuario (si no existe)..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@gmail.com', 'admin1234')"

echo "Iniciando servidor..."
# Ejecuta el comando principal (CMD) del Dockerfile (en este caso, gunicorn)
exec "$@"