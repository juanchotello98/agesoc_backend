from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.respuestaencuesta.models import Respuestaencuesta
from apps.respuestaencuesta.serializer import RespuestaencuestaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RespuestaencuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuestaencuesta.objects.all()
    serializer_class = RespuestaencuestaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pregunta', 'respuesta', 'evaluado', 'rol', 'proceso',
    'pregunta__id', 'pregunta__nombre',
    'rol__id', 'rol__nombre',
    'respuesta__id','respuesta__seleccion',
    'evaluado__id','evaluado__cedula', 'evaluado__nombre',
    'proceso__id', 'proceso__nombre', 'proceso__tipoproceso__id', 'proceso__tipoproceso__nombre']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)