from django.contrib import admin
from .models import Cliente, Veterinario, Mascota


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