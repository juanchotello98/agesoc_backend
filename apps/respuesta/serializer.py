from apps.respuesta.models import Respuesta
from rest_framework import serializers, fields



class RespuestaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Respuesta
        fields = ('id','seleccion')