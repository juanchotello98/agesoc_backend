from apps.proceso.models import Proceso
from rest_framework import serializers
from apps.tipoproceso.serializer import TipoprocesoSerializer
class ProcesoSerializer(serializers.ModelSerializer):
    usuarios = serializers.StringRelatedField(many=True)
    class Meta:
        model = Proceso
        fields = ('id','nombre','tipoproceso','usuarios')