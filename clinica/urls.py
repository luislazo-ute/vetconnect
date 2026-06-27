from rest_framework.routers import DefaultRouter
from .views import (
    VacunaViewSet,
    HabitacionViewSet,
    HospitalizacionViewSet,
    RecetaViewSet,
    DetalleRecetaViewSet,
    NotificacionViewSet,
)

router = DefaultRouter()
router.register(r'vacunas', VacunaViewSet)
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'hospitalizaciones', HospitalizacionViewSet)
router.register(r'recetas', RecetaViewSet)
router.register(r'detalles-receta', DetalleRecetaViewSet)
router.register(r'notificaciones', NotificacionViewSet)

urlpatterns = router.urls
