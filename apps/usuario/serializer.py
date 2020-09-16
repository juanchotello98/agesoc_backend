from apps.usuario.models import Usuario
from rest_framework import serializers, fields
from django.contrib.auth.hashers import make_password


class UsuarioSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Usuario
		fields = ('id','cedula','password','nombre','apellido','actividad_colectiva',
        'ips', 'cargo','rol','proceso')
	def create(self, validate_data):
		validate_data['password'] = make_password(validate_data['password'])
		return super(UsuarioSerializer, self).create(validate_data)