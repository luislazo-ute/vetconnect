from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class ClinicaPermisosTests(APITestCase):
    def setUp(self):
        self.normal = User.objects.create_user(
            username='normal', password='ClaveSegura123'
        )
        self.staff = User.objects.create_user(
            username='staff', password='ClaveSegura123', is_staff=True
        )
        self.token_normal = self._token('normal')
        self.token_staff = self._token('staff')

    def _token(self, username):
        res = self.client.post(
            '/api/token/',
            {'username': username, 'password': 'ClaveSegura123'},
            format='json',
        )
        return res.data['access']

    def _auth(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_listar_habitaciones_sin_token_401(self):
        self.client.credentials()
        res = self.client.get('/api/habitaciones/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_listar_habitaciones_usuario_normal_200(self):
        self._auth(self.token_normal)
        res = self.client.get('/api/habitaciones/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_crear_habitacion_usuario_normal_403(self):
        self._auth(self.token_normal)
        res = self.client.post(
            '/api/habitaciones/',
            {'codigo': 'H-99', 'precio_dia': '10.00'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_crear_habitacion_staff_201(self):
        self._auth(self.token_staff)
        res = self.client.post(
            '/api/habitaciones/',
            {'codigo': 'H-99', 'precio_dia': '10.00'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
