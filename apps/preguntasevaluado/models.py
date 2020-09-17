from django.db import models
from django.utils import timezone
from apps.pregunta.models import Pregunta
from apps.usuario.models import Usuario
from apps.respuesta.models import Respuesta

# Create your models here.

class Preguntasevaluado(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='preguntas_evaluado', on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, related_name='preguntas_evaluado', on_delete=models.CASCADE)
    evaluado = models.ForeignKey(Usuario, related_name='preguntas_evaluado', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['id']
    
    """def __str__(self):
        return '%d' %(self.id)"""

    