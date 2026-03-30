from rest_framework import serializers
from productos_models.models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'slug']

class ProductoSerializer(serializers.ModelSerializer):
    # Incluimos el nombre de la categoría para lectura fácil
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    # Valor calculado en el modelo
    valor_total = serializers.ReadOnlyField(source='valor_inventario_total')

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'slug', 'descripcion', 'categoria', 
            'categoria_nombre', 'imagen', 'precio', 
            'cantidad_disponible', 'valor_total', 'activo'
        ]