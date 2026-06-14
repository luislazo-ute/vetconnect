from django.urls import path
from .views import ConsultasRemotasView, ConsultaRemotaDetalleView

urlpatterns = [
    path('consultas/', ConsultasRemotasView.as_view()),
    path('consultas/<str:pk>/', ConsultaRemotaDetalleView.as_view()),
]
