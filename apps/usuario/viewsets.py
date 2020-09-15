from rest_framework import viewsets
from apps.usuario.models import Usuario
from apps.usuario.serializer import UsuarioSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cedula', 'es_evaluado','es_evaluado', 'es_coordinador']

    def perfom_create(self, serializer):
        new_user = Usuario.objects.create(username=self.request.data.get("cedula"))
        new_user.set_password(self.request.data.get("password"))
        serializer.save(password=user.password)
