from django.urls import path
from .views import ConsultasRemotasView, ConsultaRemotaDetalleView, MonitoreoSignosView, MonitoreoSignoDetalleView, NotasVozView, NotaVozDetalleView, TrackingVisitasView, TrackingVisitaDetalleView, GaleriaMascotaView, GaleriaMascotaDetalleView

urlpatterns = [
    path('consultas/', ConsultasRemotasView.as_view()),
    path('consultas/<str:pk>/', ConsultaRemotaDetalleView.as_view()),
    path('monitoreo/', MonitoreoSignosView.as_view()),
    path('monitoreo/<str:pk>/', MonitoreoSignoDetalleView.as_view()),
    path('notas-voz/', NotasVozView.as_view()),
    path('notas-voz/<str:pk>/', NotaVozDetalleView.as_view()),
    path('tracking/', TrackingVisitasView.as_view()),
    path('tracking/<str:pk>/', TrackingVisitaDetalleView.as_view()),
    path('galeria-mascota/', GaleriaMascotaView.as_view()),
    path('galeria-mascota/<str:pk>/', GaleriaMascotaDetalleView.as_view()),
]
