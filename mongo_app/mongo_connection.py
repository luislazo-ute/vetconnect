from pymongo import MongoClient
from django.conf import settings

# Cliente único de MongoDB (se conecta una sola vez).
_client = MongoClient(settings.MONGO_URI)


def get_mongo_db():
    """
    Devuelve la base de datos de MongoDB.
    El nombre se lee de settings.MONGO_DB en cada llamada, de modo que los
    tests puedan apuntar a otra base (p. ej. vetconnect_mongo_test) con
    override_settings sin afectar el código de producción.
    """
    return _client[settings.MONGO_DB]


def get_collection(nombre):
    """Devuelve una colección específica de MongoDB."""
    return get_mongo_db()[nombre]
