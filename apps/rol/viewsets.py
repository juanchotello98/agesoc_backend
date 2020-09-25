from rest_framework import viewsets
from rest_framework import filters
from apps.rol.models import Rol
from apps.rol.serializer import RolSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','rol']
