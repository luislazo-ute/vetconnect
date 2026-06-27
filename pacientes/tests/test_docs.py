from rest_framework import status
from rest_framework.test import APITestCase


class DocsTests(APITestCase):
    """La documentación OpenAPI debe generarse y ser pública."""

    def test_schema_publico(self):
        res = self.client.get('/api/schema/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_swagger_ui_publico(self):
        res = self.client.get('/api/docs/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
