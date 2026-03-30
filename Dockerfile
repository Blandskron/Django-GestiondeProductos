# 1. Usar una imagen base oficial de Python
FROM python:3.12-slim

# 2. Establecer variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Instalar dependencias del sistema
# Necesarias para compilar psycopg2 (PostgreSQL) y Pillow (Imágenes)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Instalar dependencias de Python
# Copiamos solo el archivo de requerimientos primero para aprovechar el cache de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar el script de entrada y darle permisos de ejecución
COPY ./docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# 7. Copiar el resto del código de la aplicación
COPY . .

# 8. Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# 9. Definir el script de entrada que se ejecutará al iniciar el contenedor
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# 10. Comando por defecto para correr la aplicación con un servidor WSGI de producción
CMD ["gunicorn", "config.wsgi:application", "--worker-class", "gevent", "--bind", "0.0.0.0:8000"]
