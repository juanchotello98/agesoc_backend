from django.db import models
from apps.tipoproceso.models import Tipoproceso


# Create your models here.

class Proceso(models.Model):
    proceso = models.CharField(max_length=100)
    tipoproceso = models.ForeignKey(Tipoproceso, related_name='procesos', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        #return ("%s "%(self.nombre))
        return '%d: %s' % (self.id, self.proceso)