from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    archivo_pdf = models.FileField(upload_to='proyectos_pdfs/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    autores = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('aceptado', 'Aceptado'),
            ('rechazado', 'Rechazado')
        ],
        default='pendiente'
    )

    def __str__(self):
        return self.titulo