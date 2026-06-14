from django.contrib import admin
from .models import Cliente, Veterinario, Mascota, Cita, HistorialMedico


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'created_at')
    search_fields = ('user__username', 'telefono')


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'telefono', 'is_active')
    list_filter = ('especialidad', 'is_active')
    search_fields = ('nombre', 'especialidad')


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'cliente', 'is_active')
    list_filter = ('especie', 'is_active')
    search_fields = ('nombre', 'raza')

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'veterinario', 'fecha', 'hora', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('mascota__nombre',)


@admin.register(HistorialMedico)
class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'veterinario', 'fecha', 'diagnostico')
    list_filter = ('fecha',)
    search_fields = ('mascota__nombre', 'diagnostico')