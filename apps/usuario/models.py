from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from apps.cargo.models import Cargo
from apps.rol.models import Rol
from apps.proceso.models import Proceso

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
    cargo = models.ForeignKey(Cargo, related_name='usuarios',default=4, on_delete=models.CASCADE) #default = Auxiliar o Técnico Admistrativo
    rol = models.ForeignKey(Rol, related_name='usuarios',default=1, on_delete=models.CASCADE) #default = Evaluado
    proceso = models.ForeignKey(Proceso, related_name='usuarios',default=20, on_delete=models.CASCADE) #default = GESTIÓN DE LA INFORMACIÓN
    respondio = models.BooleanField(default=False)
    evaluado = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'cedula'

    objects = ManejadorUsuario()

    REQUIRED_FIELDS = [] # cedula y password son requiridos por defecto

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return ('%d: %s'  %(self.id,self.nombre + ' ' + self.apellido))
        #return '%d: %s' % (self.id, self.nombre)


    def get_full_name(self):
        return self.nombre + ' ' + self.apellido

    def get_short_name(self):
        return self.nombre