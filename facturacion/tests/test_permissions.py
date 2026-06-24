from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class FacturacionPermisosTests(APITestCase):
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

    # --- Lectura ---

    def test_listar_servicios_sin_token_401(self):
        self.client.credentials()
        res = self.client.get('/api/servicios/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_listar_servicios_usuario_normal_200(self):
        self._auth(self.token_normal)
        res = self.client.get('/api/servicios/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_listar_productos_usuario_normal_200(self):
        self._auth(self.token_normal)
        res = self.client.get('/api/productos/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # --- Escritura ---

    def test_crear_servicio_usuario_normal_403(self):
        self._auth(self.token_normal)
        res = self.client.post(
            '/api/servicios/',
            {'nombre': 'Test', 'precio': '10.00'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_crear_servicio_staff_201(self):
        self._auth(self.token_staff)
        res = self.client.post(
            '/api/servicios/',
            {'nombre': 'Test', 'precio': '10.00', 'duracion_minutos': 30},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_crear_producto_usuario_normal_403(self):
        self._auth(self.token_normal)
        res = self.client.post(
            '/api/productos/',
            {'nombre': 'Prod Test', 'precio': '5.00', 'stock': 1},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_crear_producto_staff_201(self):
        self._auth(self.token_staff)
        # Primero crear categoria
        res_cat = self.client.post(
            '/api/categorias-producto/',
            {'nombre': 'Test Cat'},
            format='json',
        )
        res = self.client.post(
            '/api/productos/',
            {'nombre': 'Prod Test', 'precio': '5.00', 'stock': 1,
             'categoria': res_cat.data['id']},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_crear_proveedor_staff_201(self):
        self._auth(self.token_staff)
        res = self.client.post(
            '/api/proveedores/',
            {'nombre': 'Proveedor Test', 'telefono': '1234567890'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_actualizar_servicio_normal_403(self):
        self._auth(self.token_staff)
        res = self.client.post(
            '/api/servicios/',
            {'nombre': 'Test', 'precio': '10.00', 'duracion_minutos': 30},
            format='json',
        )
        servicio_id = res.data['id']

        self._auth(self.token_normal)
        res = self.client.patch(
            f'/api/servicios/{servicio_id}/',
            {'precio': '20.00'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_eliminar_servicio_normal_403(self):
        self._auth(self.token_staff)
        res = self.client.post(
            '/api/servicios/',
            {'nombre': 'Test', 'precio': '10.00', 'duracion_minutos': 30},
            format='json',
        )
        servicio_id = res.data['id']

        self._auth(self.token_normal)
        res = self.client.delete(f'/api/servicios/{servicio_id}/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
