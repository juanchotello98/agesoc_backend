from apps.respuestaencuesta.models import Respuestaencuesta
from rest_framework import serializers, fields

class RespuestaencuestaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Respuestaencuesta
        fields = ('id', 'pregunta', 'respuesta', 'evaluado', 'rol', 'proceso', 'fecha')
