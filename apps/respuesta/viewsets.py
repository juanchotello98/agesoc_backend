from rest_framework import viewsets
from rest_framework import filters
from apps.respuesta.models import Respuesta
from apps.respuesta.serializer import RespuestaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','seleccion']