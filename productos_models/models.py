from django.db import models
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self): # Corregido: era __str__, no __clase__
        return self.nombre

class Producto(models.Model):
    # Información Básica
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField(verbose_name="Descripción")
    
    # Categorización
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT, 
        related_name="productos"
    )
    
    # Imagen (Requiere: pip install Pillow)
    imagen = models.ImageField(
        upload_to="productos/%Y/%m/%d/", # Corregido: es upload_to, no upload_app
        blank=True, 
        null=True
    )
    
    # Precios y Cantidades
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )
    cantidad_disponible = models.PositiveIntegerField(
        default=0, 
        verbose_name="Stock"
    )
    
    # Metadatos de Control
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-creado']

    def __str__(self):
        return self.nombre

    @property
    def valor_inventario_total(self):
        """Calcula el valor total monetario de este producto en stock"""
        return self.precio * self.cantidad_disponible