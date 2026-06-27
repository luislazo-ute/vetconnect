from django.contrib import admin
from .models import Vacuna, Habitacion, Hospitalizacion, Receta, DetalleReceta, Notificacion


@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ['nombre_vacuna', 'mascota', 'fecha_aplicacion', 'fecha_proxima_dosis']
    list_filter = ['fecha_aplicacion', 'veterinario']
    search_fields = ['nombre_vacuna', 'mascota__nombre']


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'tipo', 'precio_dia', 'estado', 'capacidad', 'is_active']
    list_filter = ['estado', 'tipo', 'is_active']
    search_fields = ['codigo']


@admin.register(Hospitalizacion)
class HospitalizacionAdmin(admin.ModelAdmin):
    list_display = ['mascota', 'habitacion', 'fecha_ingreso', 'fecha_alta', 'is_active']
    list_filter = ['is_active', 'fecha_ingreso']
    search_fields = ['mascota__nombre', 'motivo']


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ['id', 'mascota', 'veterinario', 'fecha_emision', 'valida_hasta']
    list_filter = ['fecha_emision']
    search_fields = ['mascota__nombre']


@admin.register(DetalleReceta)
class DetalleRecetaAdmin(admin.ModelAdmin):
    list_display = ['receta', 'producto', 'dosis', 'frecuencia']
    search_fields = ['producto__nombre', 'dosis']


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'tipo', 'titulo', 'leida', 'created_at']
    list_filter = ['tipo', 'leida', 'created_at']
    search_fields = ['mensaje', 'cliente__user__username']
