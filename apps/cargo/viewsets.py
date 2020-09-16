from rest_framework import viewsets
from rest_framework import filters
from apps.cargo.models import Cargo
from apps.cargo.serializer import CargoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','nombre']

