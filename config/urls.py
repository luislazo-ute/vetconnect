from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/mongo/', include('mongo_app.urls')),
    path('api/', include('pacientes.urls')),
]
