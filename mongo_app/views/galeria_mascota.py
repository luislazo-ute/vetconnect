from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from datetime import datetime
from ..mongo_connection import get_collection
from .helpers import serializar


class GaleriaMascotaView(APIView):
    def get(self, request):
        coleccion = get_collection('galeria_mascota')
        signos = [serializar(doc) for doc in coleccion.find()]
        return Response(signos, status=status.HTTP_200_OK)

    def post(self, request):
        coleccion = get_collection('galeria_mascota')
        data = request.data.copy()
        data['created_at'] = datetime.utcnow().isoformat()
        resultado = coleccion.insert_one(data)
        nuevo = coleccion.find_one({'_id': resultado.inserted_id})
        return Response(serializar(nuevo), status=status.HTTP_201_CREATED)


class GaleriaMascotaDetalleView(APIView):
    def get(self, request, pk):
        coleccion = get_collection('galeria_mascota')
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def put(self, request, pk):
        coleccion = get_collection('galeria_mascota')
        coleccion.update_one({'_id': ObjectId(pk)}, {'$set': request.data})
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        coleccion = get_collection('galeria_mascota')
        resultado = coleccion.delete_one({'_id': ObjectId(pk)})
        if resultado.deleted_count == 0:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'mensaje': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
