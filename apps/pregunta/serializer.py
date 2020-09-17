from apps.pregunta.models import Pregunta 
from rest_framework import serializers, fields



class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('id', 'nombre')