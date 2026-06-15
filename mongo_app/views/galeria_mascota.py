from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from ..mongo_connection import get_collection
from .helpers import serializar, parse_object_id, error_response, cuerpo_invalido


class GaleriaMascotaView(APIView):
    def get(self, request):
        coleccion = get_collection('galeria_mascota')
        signos = [serializar(doc) for doc in coleccion.find()]
        return Response(signos, status=status.HTTP_200_OK)

    def post(self, request):
        error = cuerpo_invalido(request.data)
        if error:
            return error_response(error)
        coleccion = get_collection('galeria_mascota')
        data = request.data.copy()
        data['created_at'] = datetime.utcnow().isoformat()
        resultado = coleccion.insert_one(data)
        nuevo = coleccion.find_one({'_id': resultado.inserted_id})
        return Response(serializar(nuevo), status=status.HTTP_201_CREATED)


class GaleriaMascotaDetalleView(APIView):
    def get(self, request, pk):
        oid = parse_object_id(pk)
        if oid is None:
            return error_response('ID inválido.')
        coleccion = get_collection('galeria_mascota')
        doc = coleccion.find_one({'_id': oid})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def put(self, request, pk):
        oid = parse_object_id(pk)
        if oid is None:
            return error_response('ID inválido.')
        error = cuerpo_invalido(request.data)
        if error:
            return error_response(error)
        coleccion = get_collection('galeria_mascota')
        coleccion.update_one({'_id': oid}, {'$set': request.data})
        doc = coleccion.find_one({'_id': oid})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        oid = parse_object_id(pk)
        if oid is None:
            return error_response('ID inválido.')
        coleccion = get_collection('galeria_mascota')
        resultado = coleccion.delete_one({'_id': oid})
        if resultado.deleted_count == 0:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'mensaje': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
