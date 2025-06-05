from django.db import models

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    playa = models.ForeignKey(Playa, on_delete=models.CASCADE, related_name='actividades')
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    archivo = models.FileField(upload_to='archivos/', blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} en {self.playa.nombre}"