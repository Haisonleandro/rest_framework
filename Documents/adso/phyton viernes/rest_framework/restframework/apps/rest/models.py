from django.db import models

# Create your models here.
class rest(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    orden = models.TextField()
    crear_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo