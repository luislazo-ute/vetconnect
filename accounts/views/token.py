from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import CustomTokenObtainPairSerializer


class CustomTokenView(TokenObtainPairView):
    """Login que devuelve tokens enriquecidos con datos del usuario."""
    serializer_class = CustomTokenObtainPairSerializer
