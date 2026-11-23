# mensajes/models.py
from django.db import models


class Mensaje(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField("fecha de publicación", auto_now_add=True)
    autor = models.CharField("autor", max_length=50, default="Anónimo")  # nuevo

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return self.texto[:50]