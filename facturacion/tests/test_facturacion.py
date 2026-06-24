from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from pacientes.models import Cliente


class FacturacionCrudTests(APITestCase):
    def setUp(self):
        self.staff = User.objects.create_user(
            username='staff', email='staff@vet.com', password='ClaveSegura123',
            is_staff=True,
        )
        self.cliente_user = User.objects.create_user(
            username='cliente', email='cliente@vet.com', password='ClaveSegura123'
        )
        self.cliente = Cliente.objects.create(
            user=self.cliente_user, telefono='555-0000'
        )
        token = self.client.post(
            '/api/token/',
            {'username': 'staff', 'password': 'ClaveSegura123'},
            format='json',
        ).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def _crear_categoria(self):
        res = self.client.post(
            '/api/categorias-producto/',
            {'nombre': 'Medicamentos'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        return res.data['id']

    def _crear_servicio(self):
        res = self.client.post(
            '/api/servicios/',
            {'nombre': 'Consulta General', 'precio': '35.00', 'duracion_minutos': 30},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        return res.data['id']

    def _crear_producto(self, categoria_id):
        res = self.client.post(
            '/api/productos/',
            {'nombre': 'Vacuna X', 'precio': '25.00', 'stock': 10,
             'categoria': categoria_id},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        return res.data['id']

    def test_crud_servicio(self):
        # Crear
        res = self.client.post(
            '/api/servicios/',
            {'nombre': 'Baño', 'precio': '15.00', 'duracion_minutos': 20},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        servicio_id = res.data['id']

        # Leer
        res = self.client.get(f'/api/servicios/{servicio_id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['nombre'], 'Baño')

        # Listar
        res = self.client.get('/api/servicios/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('count', res.data)

    def test_crud_factura(self):
        servicio_id = self._crear_servicio()
        res = self.client.post(
            '/api/facturas/',
            {'cliente': self.cliente.id},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        factura_id = res.data['id']

        res = self.client.get(f'/api/facturas/{factura_id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['cliente'], self.cliente.id)

    def test_crud_categoria_producto(self):
        categoria_id = self._crear_categoria()
        res = self.client.get(f'/api/categorias-producto/{categoria_id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['nombre'], 'Medicamentos')

    def test_crud_producto(self):
        categoria_id = self._crear_categoria()
        producto_id = self._crear_producto(categoria_id)

        res = self.client.get(f'/api/productos/{producto_id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['nombre'], 'Vacuna X')

    def test_crud_proveedor(self):
        res = self.client.post(
            '/api/proveedores/',
            {'nombre': 'Distribuidora XYZ', 'telefono': '0987654321'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res = self.client.get('/api/proveedores/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_crud_compra(self):
        res = self.client.post(
            '/api/proveedores/',
            {'nombre': 'Distribuidora XYZ', 'telefono': '0987654321'},
            format='json',
        )
        proveedor_id = res.data['id']
        res = self.client.post(
            '/api/compras/',
            {'proveedor': proveedor_id},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        compra_id = res.data['id']

        res = self.client.get(f'/api/compras/{compra_id}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('proveedor', res.data)

    def test_crud_pago(self):
        servicio_id = self._crear_servicio()
        res = self.client.post(
            '/api/facturas/',
            {'cliente': self.cliente.id},
            format='json',
        )
        factura_id = res.data['id']

        res = self.client.post(
            '/api/pagos/',
            {'factura': factura_id, 'monto': '35.00', 'metodo_pago': 'efectivo'},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        res = self.client.get('/api/pagos/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_filtro_servicio_por_is_active(self):
        self._crear_servicio()
        self.client.post(
            '/api/servicios/',
            {'nombre': 'Inactivo', 'precio': '10.00', 'is_active': False},
            format='json',
        )
        res = self.client.get('/api/servicios/?is_active=true')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        for s in res.data['results']:
            self.assertTrue(s['is_active'])

    def test_busqueda_producto_por_nombre(self):
        categoria_id = self._crear_categoria()
        self._crear_producto(categoria_id)
        res = self.client.get('/api/productos/?search=Vacuna')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data['results']) > 0)

    def test_ordenamiento_servicio_por_precio(self):
        self._crear_servicio()
        self.client.post(
            '/api/servicios/',
            {'nombre': 'Consulta Especializada', 'precio': '60.00', 'duracion_minutos': 45},
            format='json',
        )
        res = self.client.get('/api/servicios/?ordering=precio')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        precios = [s['precio'] for s in res.data['results']]
        self.assertEqual(precios, sorted(precios))
