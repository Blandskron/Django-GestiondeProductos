from django.contrib import admin
from .models import Producto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'cantidad_disponible', 'categoria', 'activo']
    list_filter = ['activo', 'categoria', 'creado']
    list_editable = ['precio', 'cantidad_disponible', 'activo']
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ['nombre', 'descripcion']