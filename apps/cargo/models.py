from django.db import models

# Create your models here.

class Cargo():
    nombre = models.CharField(max_length=50)