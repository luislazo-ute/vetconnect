from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class PacientesCrudTests(APITestCase):
    def setUp(self):
        self.staff = User.objects.create_user(
            username='staff', email='staff@vet.com', password='ClaveSegura123',
            is_staff=True,
        )
        # Usuario "dueño" al que se asociará el Cliente.
        self.dueno = User.objects.create_user(
            username='dueno', email='dueno@vet.com', password='ClaveSegura123'
        )
        token = self.client.post(
            '/api/token/',
            {'username': 'staff', 'password': 'ClaveSegura123'},
            format='json',
        ).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def _crear_cliente(self):
        res = self.client.post(
            '/api/clientes/',
            {'user': self.dueno.id, 'telefono': '555-1234'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        return res.data['id']

    def _crear_mascota(self, cliente_id, nombre, especie):
        res = self.client.post(
            '/api/mascotas/',
            {'nombre': nombre, 'especie': especie, 'cliente': cliente_id},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        return res.data['id']

    def test_crud_cliente_y_mascota(self):
        cliente_id = self._crear_cliente()
        mascota_id = self._crear_mascota(cliente_id, 'Firulais', 'perro')

        # Lectura del detalle de la mascota creada.
        res = self.client.get(f'/api/mascotas/{mascota_id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['nombre'], 'Firulais')

    def test_listado_paginado(self):
        cliente_id = self._crear_cliente()
        self._crear_mascota(cliente_id, 'Firulais', 'perro')

        res = self.client.get('/api/mascotas/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        for key in ('count', 'next', 'previous', 'results'):
            self.assertIn(key, res.data)

    def test_filtro_por_especie(self):
        cliente_id = self._crear_cliente()
        self._crear_mascota(cliente_id, 'Firulais', 'perro')
        self._crear_mascota(cliente_id, 'Michi', 'gato')

        res = self.client.get('/api/mascotas/?especie=perro')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        especies = [m['especie'] for m in res.data['results']]
        self.assertTrue(especies)
        self.assertTrue(all(e == 'perro' for e in especies))

    def test_busqueda_por_nombre(self):
        cliente_id = self._crear_cliente()
        self._crear_mascota(cliente_id, 'Firulais', 'perro')
        self._crear_mascota(cliente_id, 'Michi', 'gato')

        res = self.client.get('/api/mascotas/?search=Firulais')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        nombres = [m['nombre'] for m in res.data['results']]
        self.assertIn('Firulais', nombres)
        self.assertNotIn('Michi', nombres)

    def test_ordenamiento_por_nombre(self):
        cliente_id = self._crear_cliente()
        self._crear_mascota(cliente_id, 'Zeus', 'perro')
        self._crear_mascota(cliente_id, 'Apolo', 'perro')

        res = self.client.get('/api/mascotas/?ordering=nombre')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        nombres = [m['nombre'] for m in res.data['results']]
        self.assertEqual(nombres, sorted(nombres))
