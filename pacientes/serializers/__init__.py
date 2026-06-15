from .cliente import ClienteSerializer
from .veterinario import VeterinarioSerializer
from .mascota import MascotaSerializer
from .cita import CitaSerializer
from .historial_medico import HistorialMedicoSerializer

__all__ = [
    'ClienteSerializer',
    'VeterinarioSerializer',
    'MascotaSerializer',
    'CitaSerializer',
    'HistorialMedicoSerializer',
]
