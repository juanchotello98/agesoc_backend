from rest_framework import viewsets
from apps.respuestaencuesta.models import Respuestaencuesta
from apps.respuestaencuesta.serializer import RespuestaencuestaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RespuestaencuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuestaencuesta.objects.all()
    serializer_class = RespuestaencuestaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pregunta', 'respuesta', 'evaluado', 'rol', 'proceso',
    'pregunta__id', 'pregunta__nombre',
    'respuesta__id','respuesta__seleccion',
    'evaluado__id','evaluado__cedula', 'evaluado__nombre',
    'rol__id', 'rol__nombre',
    'proceso__id', 'proceso__nombre', 'proceso__tipoproceso__id', 'proceso__tipoproceso__nombre']
