from django.db import models

# Create your models here.

 
class Rol(models.Model):
    rol = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        #return ("%s "%(self.nombre))
        return '%d: %s' % (self.id, self.rol)