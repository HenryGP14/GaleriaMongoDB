from djongo import models

class Publicacion(models.Model):
    fecha = models.DateField()
    direccion = models.CharField(max_length = 100, null = False, blank = True)
    descripcion = models.CharField(max_length = 60, null = False, blank = True)
    ruta_publicacion = models.ImageField(upload_to="publicacion", null = True, blank = False)
