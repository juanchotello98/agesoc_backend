from apps.pregunta.models import Pregunta 
from rest_framework import serializers, fields



class PreguntaSerializer(serializers.ModelSerializer):
    preguntas_evaluado = serializers.StringRelatedField(many=True)
    class Meta:
        model = Pregunta
        fields = ('id', 'nombre','preguntas_evaluado')