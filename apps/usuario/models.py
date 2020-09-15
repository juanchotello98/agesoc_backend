from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)


# Create your models here.
class ManejadorUsuario(BaseUserManager):

    def create_user(self, cedula, password) :
        if not cedula:  
            raise ValueError('Los usuarios deben tener una cedula valida.')

        usuario = self.model(cedula=cedula, **extra_ields)
        usuario.set_password(password)
        usuario.save(usign=self._db)
        return usuario

    def create_superuser(self, cedula, password):
        usuario = self.create_user(cedula, password=password, *extra_fields)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(usign=self._db)
        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):
    cedula = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    actividad_colectiva = models.CharField(max_length=50)
    ips = models.CharField(max_length=50)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'cedula'

    objects = ManejadorUsuario()

    REQUIRED_FIELDS = [] # cedula y password son requiridos por defecto


    def get_full_name(self):
        return self.nombre + ' ' + self.apellido

    def get_short_name(self):
        return self.nombre