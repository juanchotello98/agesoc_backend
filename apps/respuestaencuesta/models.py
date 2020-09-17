from django.db import models
from django.utils import timezone
from apps.pregunta.models import Pregunta
from apps.usuario.models import Usuario
from apps.respuesta.models import Respuesta
from apps.rol.models import Rol
from apps.proceso.models import Proceso

# Create your models here.

class Respuestaencuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuesta_encuesta', on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, related_name='respuesta_encuesta', on_delete=models.CASCADE)
    evaluado = models.ForeignKey(Usuario, related_name='respuesta_encuesta', on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, related_name='respuesta_encuesta', on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso, related_name='respuesta_encuesta', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    