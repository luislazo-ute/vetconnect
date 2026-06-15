from bson import ObjectId
from bson.errors import InvalidId
from rest_framework import status
from rest_framework.response import Response


def serializar(doc):
    """Convierte el _id de ObjectId a string para poder devolverlo como JSON."""
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc


def parse_object_id(pk):
    """Devuelve ObjectId(pk) o None si el id no tiene un formato válido."""
    try:
        return ObjectId(pk)
    except (InvalidId, TypeError):
        return None


def error_response(mensaje, codigo=status.HTTP_400_BAD_REQUEST):
    """Respuesta de error uniforme para las vistas de Mongo."""
    return Response({'error': mensaje}, status=codigo)


def cuerpo_invalido(data, requeridos=None):
    """
    Valida el cuerpo de un POST/PUT.
    Devuelve un mensaje de error si el cuerpo está vacío o faltan campos
    requeridos; devuelve None si todo está bien.
    """
    if not data:
        return 'El cuerpo de la petición no puede estar vacío.'
    if requeridos:
        faltantes = [campo for campo in requeridos if not data.get(campo)]
        if faltantes:
            return f'Faltan campos obligatorios: {", ".join(faltantes)}.'
    return None
