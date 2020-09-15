from apps.proceso.models import Proceso
from rest_framework import serializers, fields

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = '__all__'