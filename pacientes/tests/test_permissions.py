from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class PermisosTests(APITestCase):
    def setUp(self):
        self.normal = User.objects.create_user(
            username='normal', email='normal@vet.com', password='ClaveSegura123'
        )
        self.staff = User.objects.create_user(
            username='staff', email='staff@vet.com', password='ClaveSegura123',
            is_staff=True,
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

    # --- Lectura ---

    def test_listar_clientes_sin_token_401(self):
        self.client.credentials()
        res = self.client.get('/api/clientes/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_listar_clientes_usuario_normal_200(self):
        self._auth(self.token_normal)
        res = self.client.get('/api/clientes/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # --- Escritura ---

    def test_crear_veterinario_usuario_normal_403(self):
        self._auth(self.token_normal)
        data = {
            'nombre': 'Dr. Test', 'especialidad': 'General',
            'telefono': '123', 'email': 'vet@vet.com',
        }
        res = self.client.post('/api/veterinarios/', data, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_crear_veterinario_staff_201(self):
        self._auth(self.token_staff)
        data = {
            'nombre': 'Dr. Test', 'especialidad': 'General',
            'telefono': '123', 'email': 'vet@vet.com',
        }
        res = self.client.post('/api/veterinarios/', data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    # --- Gestión de usuarios (IsAdminUser) ---

    def test_users_usuario_normal_403(self):
        self._auth(self.token_normal)
        self.assertEqual(
            self.client.get('/api/users/').status_code,
            status.HTTP_403_FORBIDDEN,
        )
        res = self.client.post(
            '/api/users/',
            {'username': 'x', 'email': 'x@vet.com'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_users_staff_200(self):
        self._auth(self.token_staff)
        res = self.client.get('/api/users/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
