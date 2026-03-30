from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from productos_models.models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    # Aplicamos el tag "Productos" a todos los métodos del ViewSet
    list=extend_schema(tags=['Productos'], description="Obtener lista de todos los productos."),
    retrieve=extend_schema(tags=['Productos'], description="Obtener detalles de un producto específico."),
    create=extend_schema(
        tags=['Productos'],
        description="Crear un nuevo producto con imagen.",
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "nombre": {"type": "string"},
                    "slug": {"type": "string"},
                    "descripcion": {"type": "string"},
                    "categoria": {"type": "integer", "description": "ID de la categoría"},
                    "imagen": {"type": "string", "format": "binary"},
                    "precio": {"type": "number", "format": "float"},
                    "cantidad_disponible": {"type": "integer"},
                    "activo": {"type": "boolean"},
                },
                "required": ["nombre", "slug", "categoria", "precio"],
            }
        }
    ),
    update=extend_schema(
        tags=['Productos'],
        description="Actualizar un producto (incluyendo la imagen).",
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "imagen": {"type": "string", "format": "binary"},
                    "nombre": {"type": "string"},
                    "precio": {"type": "number", "format": "float"},
                }
            }
        }
    ),
    partial_update=extend_schema(tags=['Productos']),
    destroy=extend_schema(tags=['Productos'])
)
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@extend_schema_view(
    # Agrupamos los métodos de categorías bajo el tag "Categorías"
    list=extend_schema(tags=['Categorías']),
    retrieve=extend_schema(tags=['Categorías']),
    create=extend_schema(tags=['Categorías']),
    update=extend_schema(tags=['Categorías']),
    partial_update=extend_schema(tags=['Categorías']),
    destroy=extend_schema(tags=['Categorías']),
)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer