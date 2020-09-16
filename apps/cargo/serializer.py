from apps.cargo.models import Cargo
from rest_framework import serializers, fields



class CargoSerializer(serializers.ModelSerializer):
	usuarios = serializers.StringRelatedField(many=True)
	class Meta: 
		model = Cargo
		fields = ('id','nombre','usuarios')