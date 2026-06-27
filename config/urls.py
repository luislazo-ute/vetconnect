from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from accounts.views import CustomTokenView
from pacientes.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check, name='health_check'),

    # JWT (login disponible como /api/token/ y como /api/auth/login/)
    path('api/token/', CustomTokenView.as_view(), name='token_obtain_pair'),
    path('api/auth/login/', CustomTokenView.as_view(), name='auth_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Documentación OpenAPI / Swagger / Redoc
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/', include('accounts.urls')),
    path('api/mongo/', include('mongo_app.urls')),
    path('api/', include('pacientes.urls')),
    path('api/', include('facturacion.urls')),
    path('api/', include('clinica.urls')),
]
