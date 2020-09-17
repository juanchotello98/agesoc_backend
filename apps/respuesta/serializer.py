from apps.respuesta.models import Respuesta
from rest_framework import serializers, fields



class RespuestaSerializer(serializers.ModelSerializer):
    preguntas_evaluado = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Respuesta
        fields = ('id','seleccion','preguntas_evaluado')