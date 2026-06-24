from rest_framework.routers import DefaultRouter
from .views import (
    ServicioViewSet,
    FacturaViewSet,
    DetalleFacturaViewSet,
    PagoViewSet,
    CategoriaProductoViewSet,
    ProductoViewSet,
    ProveedorViewSet,
    CompraViewSet,
    DetalleCompraViewSet,
)

router = DefaultRouter()
router.register(r'servicios', ServicioViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'detalles-factura', DetalleFacturaViewSet)
router.register(r'pagos', PagoViewSet)
router.register(r'categorias-producto', CategoriaProductoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'detalles-compra', DetalleCompraViewSet)

urlpatterns = router.urls
