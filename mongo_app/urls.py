from django.urls import path
from .views import ConsultasRemotasView, ConsultaRemotaDetalleView, MonitoreoSignosView, MonitoreoSignoDetalleView

urlpatterns = [
    path('consultas/', ConsultasRemotasView.as_view()),
    path('consultas/<str:pk>/', ConsultaRemotaDetalleView.as_view()),
    path('monitoreo/', MonitoreoSignosView.as_view()),
    path('monitoreo/<str:pk>/', MonitoreoSignoDetalleView.as_view()),
]
