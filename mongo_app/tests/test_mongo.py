from django.conf import settings
from django.contrib.auth.models import User
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase

# Base de datos Mongo dedicada a los tests para no contaminar la real.
TEST_MONGO_DB = settings.MONGO_DB + '_test'


@override_settings(MONGO_DB=TEST_MONGO_DB)
class MongoTests(APITestCase):
    url = '/api/mongo/consultas/'

    def setUp(self):
        self.user = User.objects.create_user(
            username='mongouser', email='mongo@vet.com', password='ClaveSegura123'
        )
        token = self.client.post(
            '/api/token/',
            {'username': 'mongouser', 'password': 'ClaveSegura123'},
            format='json',
        ).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def tearDown(self):
        # Elimina por completo la base de prueba tras cada test.
        from mongo_app.mongo_connection import get_mongo_db
        db = get_mongo_db()
        db.client.drop_database(db.name)

    def test_crear_y_listar_documento(self):
        crear = self.client.post(
            self.url, {'motivo': 'Dolor de patita'}, format='json'
        )
        self.assertEqual(crear.status_code, status.HTTP_201_CREATED)
        creado_id = crear.data['_id']

        listar = self.client.get(self.url)
        self.assertEqual(listar.status_code, status.HTTP_200_OK)
        ids = [doc['_id'] for doc in listar.data]
        self.assertIn(creado_id, ids)

    def test_id_invalido_devuelve_400(self):
        res = self.client.get(self.url + 'id-invalido-123/')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_cuerpo_vacio_devuelve_400(self):
        res = self.client.post(self.url, {}, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_acceso_sin_token_401(self):
        self.client.credentials()  # quita la autenticación
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
