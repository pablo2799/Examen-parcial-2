from django.db import models

# Create your models here.
class comentarios(models.Model):
    observacion=models.TextField(max_length=500, help_text="Introduce la observacion")
    direccionip=models.CharField(max_length=15, help_text="Introduce la direccion IP")
    equipo=models.CharField(max_length=30, help_text="Introduce el nombre del equipo")
    def __str__(self):
        return self.observacion