from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from bson import ObjectId
from datetime import datetime
from .mongo_connection import get_collection


# Función auxiliar: convierte el _id de Mongo (ObjectId) a texto
def serializar(doc):
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc


# ===== CONSULTAS REMOTAS (telemedicina - cámara) =====
class ConsultasRemotasView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        coleccion = get_collection('consultas_remotas')
        consultas = [serializar(doc) for doc in coleccion.find()]
        return Response(consultas, status=status.HTTP_200_OK)

    def post(self, request):
        coleccion = get_collection('consultas_remotas')
        data = request.data.copy()
        data['fecha'] = datetime.utcnow().isoformat()
        data['estado'] = data.get('estado', 'pendiente')
        resultado = coleccion.insert_one(data)
        nuevo = coleccion.find_one({'_id': resultado.inserted_id})
        return Response(serializar(nuevo), status=status.HTTP_201_CREATED)


class ConsultaRemotaDetalleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        coleccion = get_collection('consultas_remotas')
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrada'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def put(self, request, pk):
        coleccion = get_collection('consultas_remotas')
        coleccion.update_one({'_id': ObjectId(pk)}, {'$set': request.data})
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrada'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        coleccion = get_collection('consultas_remotas')
        resultado = coleccion.delete_one({'_id': ObjectId(pk)})
        if resultado.deleted_count == 0:
            return Response({'error': 'No encontrada'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'mensaje': 'Eliminada'}, status=status.HTTP_204_NO_CONTENT)


# ===== MONITOREO DE SIGNOS (sensores IoT) =====
class MonitoreoSignosView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        coleccion = get_collection('monitoreo_signos')
        signos = [serializar(doc) for doc in coleccion.find()]
        return Response(signos, status=status.HTTP_200_OK)

    def post(self, request):
        coleccion = get_collection('monitoreo_signos')
        data = request.data.copy()
        data['timestamp'] = datetime.utcnow().isoformat()
        data['alerta'] = data.get('alerta', False)
        resultado = coleccion.insert_one(data)
        nuevo = coleccion.find_one({'_id': resultado.inserted_id})
        return Response(serializar(nuevo), status=status.HTTP_201_CREATED)


class MonitoreoSignoDetalleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        coleccion = get_collection('monitoreo_signos')
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def put(self, request, pk):
        coleccion = get_collection('monitoreo_signos')
        coleccion.update_one({'_id': ObjectId(pk)}, {'$set': request.data})
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        coleccion = get_collection('monitoreo_signos')
        resultado = coleccion.delete_one({'_id': ObjectId(pk)})
        if resultado.deleted_count == 0:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'mensaje': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

# ===== NOTAS DE VOZ  =====
class NotasVozView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        coleccion = get_collection('notas_voz_consulta')
        signos = [serializar(doc) for doc in coleccion.find()]
        return Response(signos, status=status.HTTP_200_OK)

    def post(self, request):
        coleccion = get_collection('notas_voz_consulta')
        data = request.data.copy()
        data['fecha'] = datetime.utcnow().isoformat()
        resultado = coleccion.insert_one(data)
        nuevo = coleccion.find_one({'_id': resultado.inserted_id})
        return Response(serializar(nuevo), status=status.HTTP_201_CREATED)


class NotaVozDetalleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        coleccion = get_collection('notas_voz_consulta')
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def put(self, request, pk):
        coleccion = get_collection('notas_voz_consulta')
        coleccion.update_one({'_id': ObjectId(pk)}, {'$set': request.data})
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        coleccion = get_collection('notas_voz_consulta')
        resultado = coleccion.delete_one({'_id': ObjectId(pk)})
        if resultado.deleted_count == 0:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'mensaje': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)


# ===== RASTREO GPS  =====
class TrackingVisitasView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        coleccion = get_collection('tracking_visitas')
        signos = [serializar(doc) for doc in coleccion.find()]
        return Response(signos, status=status.HTTP_200_OK)

    def post(self, request):
        coleccion = get_collection('tracking_visitas')
        data = request.data.copy()
        data['fecha'] = datetime.utcnow().isoformat()
        data['estado'] = data.get('estado', 'en_camino')
        resultado = coleccion.insert_one(data)
        nuevo = coleccion.find_one({'_id': resultado.inserted_id})
        return Response(serializar(nuevo), status=status.HTTP_201_CREATED)


class TrackingVisitaDetalleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        coleccion = get_collection('tracking_visitas')
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def put(self, request, pk):
        coleccion = get_collection('tracking_visitas')
        coleccion.update_one({'_id': ObjectId(pk)}, {'$set': request.data})
        doc = coleccion.find_one({'_id': ObjectId(pk)})
        if not doc:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializar(doc), status=status.HTTP_200_OK)

    def delete(self, request, pk):
        coleccion = get_collection('tracking_visitas')
        resultado = coleccion.delete_one({'_id': ObjectId(pk)})
        if resultado.deleted_count == 0:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'mensaje': 'Eliminado'}, status=status.HTTP_204_NO_CONTENT)

# ===== GALERIA DE MASCOTAS  =====
class GaleriaMascotaView(APIView):
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

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
