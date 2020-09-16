from apps.rol.models import Rol
from rest_framework import serializers, fields


class RolSerializer(serializers.ModelSerializer):
	usuarios = serializers.StringRelatedField(many=True)
	class Meta: 
		model = Rol
		fields = ('id', 'nombre', 'usuarios')