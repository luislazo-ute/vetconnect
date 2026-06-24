from django.contrib import admin
from .models import (
    Servicio, Factura, DetalleFactura, Pago,
    CategoriaProducto, Producto, Proveedor, Compra, DetalleCompra,
)


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'duracion_minutos', 'is_active')
    search_fields = ('nombre',)


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total', 'pagada')
    list_filter = ('pagada', 'fecha')
    search_fields = ('cliente__user__username',)


@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'servicio', 'cantidad', 'precio_unitario', 'subtotal')


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('factura', 'monto', 'fecha_pago', 'metodo_pago')
    list_filter = ('metodo_pago',)


@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'is_active')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'is_active')
    list_filter = ('categoria', 'is_active')
    search_fields = ('nombre',)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'is_active')
    search_fields = ('nombre',)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'fecha', 'total', 'estado')
    list_filter = ('estado',)


@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
