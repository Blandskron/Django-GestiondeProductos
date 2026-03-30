# Django - Gestión de Productos API

Proyecto educativo para crear una API RESTful de gestión de productos e inventario para una tienda online o punto de venta.

## ✨ Características

*   **API RESTful Completa**: Endpoints para operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en Productos y Categorías.
*   **Documentación Automática**: Interfaz de Swagger UI generada automáticamente para explorar y probar la API.
*   **Contenerización con Docker**: La aplicación y su base de datos PostgreSQL están completamente dockerizadas para un despliegue consistente.
*   **Orquestación con Docker Compose**: Levanta todo el entorno (API + Base de Datos) con un solo comando.
*   **Configuración Segura**: Uso de variables de entorno (`.env`) para gestionar configuraciones y secretos.
*   **Servidor de Producción**: Utiliza Gunicorn y Gevent para un rendimiento eficiente y asíncrono.
*   **Gestión de Archivos Estáticos**: `Whitenoise` para servir archivos estáticos de forma optimizada en producción.
*   **CORS Habilitado**: Permite que la API sea consumida desde cualquier cliente web.
*   **Script de Arranque Automatizado**: Aplica migraciones, recolecta estáticos y crea un superusuario al iniciar el contenedor.

## 🛠️ Tecnologías Utilizadas

*   **Backend**: Django, Django REST Framework
*   **Base de Datos**: PostgreSQL
*   **Servidor WSGI**: Gunicorn
*   **Workers Asíncronos**: Gevent
*   **Documentación API**: drf-spectacular (Swagger/OpenAPI)
*   **Contenerización**: Docker, Docker Compose
*   **Servidor de Estáticos**: Whitenoise
*   **Variables de Entorno**: python-dotenv
*   **CORS**: django-cors-headers

## 🚀 Cómo Empezar

Sigue estos pasos para levantar el proyecto en tu entorno local.

### Prerrequisitos

*   Docker
*   Docker Compose (generalmente incluido con Docker Desktop)

### Instalación

1.  **Clona el repositorio:**
    ```sh
    git clone https://github.com/tu-usuario/Django-GestiondeProductos.git
    cd Django-GestiondeProductos
    ```

2.  **Crea el archivo de variables de entorno:**
    Copia el archivo de ejemplo `.env.example` y renómbralo a `.env`. Luego, ajusta los valores si es necesario (especialmente `SECRET_KEY`).

    ```sh
    cp .env.example .env
    ```

3.  **Levanta los servicios con Docker Compose:**
    Este comando construirá las imágenes (si es necesario), creará los contenedores y los iniciará.

    ```sh
    docker-compose up --build
    ```
    La opción `--build` fuerza la reconstrucción de la imagen de la API si has hecho cambios en el código.

¡Y listo! La aplicación estará corriendo.

## 🌐 Endpoints Principales

*   **API**: `http://localhost:8000/api/v1/`
*   **Documentación (Swagger UI)**: `http://localhost:8000/` (cualquier ruta 404 redirige aquí)
*   **Panel de Administración de Django**: `http://localhost:8000/admin/`
    *   **Usuario**: `admin`
    *   **Contraseña**: `admin1234`

## 🐳 Comandos de Docker

Si necesitas construir y publicar tu propia imagen en Docker Hub:

1.  **Iniciar sesión en Docker Hub:**
    ```sh
    docker login
    ```

2.  **Construir la imagen (ejemplo):**
    ```sh
    docker build -t blandskron/gestordeproductos:latest .
    ```

3.  **Publicar la imagen:**
    ```sh
    docker push blandskron/gestordeproductos:latest
    ```
