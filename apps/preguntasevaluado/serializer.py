from apps.preguntasevaluado.models import Preguntasevaluado
from rest_framework import serializers, fields

class PreguntasevaluadoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Preguntasevaluado
        fields = ('id','pregunta','respuesta','evaluado', 'fecha')


