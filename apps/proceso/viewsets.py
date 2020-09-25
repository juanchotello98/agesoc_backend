from rest_framework import viewsets
from rest_framework import filters
from apps.proceso.models import Proceso
from apps.proceso.serializer import ProcesoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','proceso','tipoproceso','tipoproceso__nombre','tipoproceso__id']