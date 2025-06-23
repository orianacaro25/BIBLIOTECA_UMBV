from django.db import models
from django.contrib.auth.models import User
from proyectos.models import Proyecto

class Evaluacion(models.Model):
   class Evaluacion(models.Model):
    CATEGORIAS = [
        
        #EJEMPLOS (DEBEN COORDINARSE CON LA UNIVERSIDAD)
        ('aeronautica civil', 'Aeronáutica Civil'),
        ('humanidades', 'Humanidades'),
        ('tecnologia', 'Tecnología'),
    ]
    proyecto = models.OneToOneField(Proyecto, on_delete=models.CASCADE)
    evaluador = models.ForeignKey(User, on_delete=models.CASCADE)
    comentarios = models.TextField()
    nota = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    fecha_evaluacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluación de {self.proyecto.titulo}"