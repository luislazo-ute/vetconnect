from pymongo import MongoClient
from django.conf import settings

# Cliente único de MongoDB (se conecta una sola vez)
_client = MongoClient(settings.MONGO_URI)
_db = _client[settings.MONGO_DB]


def get_mongo_db():
    """Devuelve la base de datos de MongoDB para usar en las vistas."""
    return _db


def get_collection(nombre):
    """Devuelve una colección específica de MongoDB."""
    return _db[nombre]
