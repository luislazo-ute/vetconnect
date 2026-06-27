from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from pacientes.models import Cliente, Mascota, Veterinario
from facturacion.models import CategoriaProducto, Producto
from clinica.models import Habitacion


class ClinicaCrudTests(APITestCase):
    def setUp(self):
        self.staff = User.objects.create_user(
            username='staff', email='staff@vet.com', password='ClaveSegura123',
            is_staff=True,
        )
        self.dueno = User.objects.create_user(
            username='dueno', email='dueno@vet.com', password='ClaveSegura123'
        )
        self.cliente = Cliente.objects.create(user=self.dueno, telefono='555-0000')
        self.mascota = Mascota.objects.create(
            nombre='Firulais', especie='perro', cliente=self.cliente
        )
        self.vet = Veterinario.objects.create(
            nombre='Dr. House', especialidad='General',
            telefono='123', email='house@vet.com',
        )
        token = self.client.post(
            '/api/token/',
            {'username': 'staff', 'password': 'ClaveSegura123'},
            format='json',
        ).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_crud_habitacion_y_paginacion(self):
        res = self.client.post(
            '/api/habitaciones/',
            {'codigo': 'H-01', 'tipo': 'canil', 'precio_dia': '20.00'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        hid = res.data['id']

        detalle = self.client.get(f'/api/habitaciones/{hid}/')
        self.assertEqual(detalle.status_code, status.HTTP_200_OK)
        self.assertEqual(detalle.data['codigo'], 'H-01')

        lista = self.client.get('/api/habitaciones/')
        for key in ('count', 'next', 'previous', 'results'):
            self.assertIn(key, lista.data)

    def test_crud_vacuna(self):
        res = self.client.post(
            '/api/vacunas/',
            {'mascota': self.mascota.id, 'veterinario': self.vet.id,
             'nombre_vacuna': 'Antirrábica', 'fecha_aplicacion': '2026-06-01'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['nombre_vacuna'], 'Antirrábica')

    def test_crud_hospitalizacion(self):
        habitacion = Habitacion.objects.create(codigo='H-02', precio_dia='15.00')
        res = self.client.post(
            '/api/hospitalizaciones/',
            {'mascota': self.mascota.id, 'habitacion': habitacion.id,
             'veterinario': self.vet.id,
             'fecha_ingreso': '2026-06-01T10:00:00Z', 'motivo': 'Observación'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['habitacion_codigo'], 'H-02')

    def test_crud_receta_y_detalle(self):
        # Receta (FK opcional a cita; aquí se omite)
        receta = self.client.post(
            '/api/recetas/',
            {'mascota': self.mascota.id, 'veterinario': self.vet.id,
             'fecha_emision': '2026-06-01T09:00:00Z', 'valida_hasta': '2026-07-01'},
            format='json',
        )
        self.assertEqual(receta.status_code, status.HTTP_201_CREATED)
        receta_id = receta.data['id']

        # Detalle de receta: usa un Producto de la app facturacion
        categoria = CategoriaProducto.objects.create(nombre='Medicamentos')
        producto = Producto.objects.create(
            nombre='Amoxicilina', categoria=categoria, precio_venta='5.00',
        )
        detalle = self.client.post(
            '/api/detalles-receta/',
            {'receta': receta_id, 'producto': producto.id,
             'dosis': '1 tableta', 'frecuencia': 'cada 8h', 'duracion_dias': 7},
            format='json',
        )
        self.assertEqual(detalle.status_code, status.HTTP_201_CREATED)
        self.assertEqual(detalle.data['duracion_dias'], 7)
        self.assertEqual(detalle.data['producto_nombre'], 'Amoxicilina')

    def test_crud_notificacion(self):
        res = self.client.post(
            '/api/notificaciones/',
            {'cliente': self.cliente.id, 'tipo': 'recordatorio',
             'titulo': 'Cita próxima', 'mensaje': 'Recuerde su cita del lunes.'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['titulo'], 'Cita próxima')

    def test_filtro_habitacion_por_estado(self):
        self.client.post(
            '/api/habitaciones/',
            {'codigo': 'H-10', 'precio_dia': '20.00'},  # estado por defecto: disponible
            format='json',
        )
        self.client.post(
            '/api/habitaciones/',
            {'codigo': 'H-11', 'precio_dia': '20.00', 'estado': 'ocupada'},
            format='json',
        )
        res = self.client.get('/api/habitaciones/?estado=disponible')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        estados = [h['estado'] for h in res.data['results']]
        self.assertTrue(estados)
        self.assertTrue(all(e == 'disponible' for e in estados))
