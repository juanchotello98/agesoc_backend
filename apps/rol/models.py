from django.db import models

# Create your models here.

 
class Rol(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        #return ("%s "%(self.nombre))
        return '%d: %s' % (self.id, self.nombre)