from rest_framework import viewsets
from apps.preguntasevaluado.models import Preguntasevaluado
from apps.preguntasevaluado.serializer import PreguntasevaluadoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PreguntasevaluadoViewSet(viewsets.ModelViewSet):
    queryset = Preguntasevaluado.objects.all()
    serializer_class = PreguntasevaluadoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pregunta', 'respuesta', 'evaluado',
    'pregunta__id', 'pregunta__nombre',
    'respuesta__id','respuesta__seleccion',
    'evaluado__id','evaluado__cedula', 'evaluado__nombre']