from apps.rol.models import Rol
from rest_framework import serializers, fields


class RolSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Rol
		fields = ('id', 'rol')