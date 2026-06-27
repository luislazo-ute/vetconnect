from django.contrib import admin
from .models import Vacuna, Habitacion, Hospitalizacion, Receta, DetalleReceta, Notificacion


@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'mascota', 'fecha_aplicacion', 'fecha_proxima']
    list_filter = ['fecha_aplicacion', 'veterinario']
    search_fields = ['nombre', 'mascota__nombre']


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['numero', 'tipo', 'precio_dia', 'estado', 'capacidad']
    list_filter = ['estado', 'tipo']
    search_fields = ['numero']


@admin.register(Hospitalizacion)
class HospitalizacionAdmin(admin.ModelAdmin):
    list_display = ['mascota', 'habitacion', 'fecha_ingreso', 'fecha_salida', 'is_active']
    list_filter = ['is_active', 'fecha_ingreso']
    search_fields = ['mascota__nombre', 'motivo']


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ['id', 'mascota', 'veterinario', 'fecha']
    list_filter = ['fecha']
    search_fields = ['mascota__nombre']


@admin.register(DetalleReceta)
class DetalleRecetaAdmin(admin.ModelAdmin):
    list_display = ['receta', 'producto', 'dosis', 'frecuencia']
    search_fields = ['producto__nombre', 'dosis']


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'tipo', 'leida', 'created_at']
    list_filter = ['tipo', 'leida', 'created_at']
    search_fields = ['mensaje', 'cliente__user__username']
