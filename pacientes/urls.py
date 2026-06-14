from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, VeterinarioViewSet, MascotaViewSet, CitaViewSet, HistorialMedicoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'veterinarios', VeterinarioViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'historiales', HistorialMedicoViewSet)

urlpatterns = router.urls
