from apps.proceso.models import Proceso
from rest_framework import serializers

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = ('id','nombre','tipoproceso')