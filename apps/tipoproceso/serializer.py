from apps.tipoproceso.models import Tipoproceso
from rest_framework import serializers, fields

class TipoprocesoSerializer(serializers.ModelSerializer):
    procesos = serializers.StringRelatedField(many=True)
    class Meta:
        model = Tipoproceso
        fields = ['id','nombre','procesos']

        