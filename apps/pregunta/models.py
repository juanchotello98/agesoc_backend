from django.db import models

# Create your models here.

class Pregunta(models.Model):
    nombre = models.CharField(max_length=400)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return '%d: %s' %(self.id, self.nombre)
        