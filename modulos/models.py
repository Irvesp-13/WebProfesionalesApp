from django.db import models

class Modulo(models.Model):
    # Atributos de la clase
    nombre = models.CharField(max_length = 100)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre