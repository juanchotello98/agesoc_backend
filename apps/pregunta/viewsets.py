from rest_framework import viewsets
from rest_framework import filters
from apps.pregunta.models import Pregunta
from apps.pregunta.serializer import PreguntaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'nombre']