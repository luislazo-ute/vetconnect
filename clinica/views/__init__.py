from .vacuna import VacunaViewSet
from .habitacion import HabitacionViewSet
from .hospitalizacion import HospitalizacionViewSet
from .receta import RecetaViewSet
from .detalle_receta import DetalleRecetaViewSet
from .notificacion import NotificacionViewSet

__all__ = [
    'VacunaViewSet',
    'HabitacionViewSet',
    'HospitalizacionViewSet',
    'RecetaViewSet',
    'DetalleRecetaViewSet',
    'NotificacionViewSet',
]
