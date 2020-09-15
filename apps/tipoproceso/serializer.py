from apps.tipoproceso.models import Tipoproceso
from rest_framework import serializers, fields

class TipoprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipoproceso
        fields = '__all__'