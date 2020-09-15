from rest_framework import viewsets
from apps.tipoproceso.models import Tipoproceso
from apps.tipoproceso.serializer import TipoprocesoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TipoprocesoViewSet(viewsets.ModelViewSet):
    queryset = Tipoproceso.objects.all()
    serializer_class = TipoprocesoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']