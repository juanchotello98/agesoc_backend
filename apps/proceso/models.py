from django.db import models
from apps.tipoproceso.models import Tipoproceso
from django.utils import timezone

# Create your models here.

class Proceso(models.Model):
    nombre = models.CharField(max_length=100)
    id_tipoproceso = models.ForeignKey(Tipoproceso, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s "%(self.nombre))