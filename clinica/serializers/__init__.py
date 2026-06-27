from .vacuna import VacunaSerializer
from .habitacion import HabitacionSerializer
from .hospitalizacion import HospitalizacionSerializer
from .receta import RecetaSerializer
from .detalle_receta import DetalleRecetaSerializer
from .notificacion import NotificacionSerializer

__all__ = [
    'VacunaSerializer',
    'HabitacionSerializer',
    'HospitalizacionSerializer',
    'RecetaSerializer',
    'DetalleRecetaSerializer',
    'NotificacionSerializer',
]
