from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = '/api/auth/register/'
        self.token_url = '/api/token/'
        self.logout_url = '/api/auth/logout/'
        self.refresh_url = '/api/token/refresh/'
        # Usuario existente para probar duplicados y login.
        self.existing = User.objects.create_user(
            username='existente',
            email='existente@vet.com',
            password='ClaveSegura123',
        )

    # --- Registro ---

    def test_registro_valido_devuelve_tokens(self):
        data = {
            'username': 'nuevo',
            'email': 'nuevo@vet.com',
            'password': 'ClaveSegura123',
            'password2': 'ClaveSegura123',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertTrue(User.objects.filter(username='nuevo').exists())

    def test_registro_password_no_coincide(self):
        data = {
            'username': 'otro',
            'email': 'otro@vet.com',
            'password': 'ClaveSegura123',
            'password2': 'NoCoincide123',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registro_username_duplicado(self):
        data = {
            'username': 'existente',
            'email': 'distinto@vet.com',
            'password': 'ClaveSegura123',
            'password2': 'ClaveSegura123',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registro_email_duplicado(self):
        data = {
            'username': 'distinto',
            'email': 'existente@vet.com',
            'password': 'ClaveSegura123',
            'password2': 'ClaveSegura123',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # --- Login ---

    def test_login_correcto_devuelve_datos_usuario(self):
        data = {'username': 'existente', 'password': 'ClaveSegura123'}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], 'existente')
        self.assertEqual(response.data['user']['email'], 'existente@vet.com')
        self.assertIn('is_staff', response.data['user'])

    def test_login_incorrecto_401(self):
        data = {'username': 'existente', 'password': 'claveincorrecta'}
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # --- Logout / blacklist ---

    def test_logout_blacklistea_refresh(self):
        login = self.client.post(
            self.token_url,
            {'username': 'existente', 'password': 'ClaveSegura123'},
            format='json',
        )
        access = login.data['access']
        refresh = login.data['refresh']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        logout = self.client.post(
            self.logout_url, {'refresh': refresh}, format='json'
        )
        self.assertEqual(logout.status_code, status.HTTP_200_OK)

        # Reutilizar el refresh ya en blacklist debe fallar.
        self.client.credentials()  # limpia el header
        reuse = self.client.post(
            self.refresh_url, {'refresh': refresh}, format='json'
        )
        self.assertEqual(reuse.status_code, status.HTTP_401_UNAUTHORIZED)
