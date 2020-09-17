from django.db import models

# Create your models here.

class Respuesta(models.Model):
    seleccion = models.IntegerField()
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return '%d: %d' %(self.id, self.seleccion)