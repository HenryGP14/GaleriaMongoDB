from djongo import models
from fernet_fields import EncryptedTextField

# Create your models here.
class Usuario(models.Model):
    nombres = models.CharField(max_length = 60, null = False, blank = True)
    nomusuario = models.CharField(max_length = 25, null = False, blank = True)
    contrasenia = models.CharField(max_length = 25, null = False, blank = True)
    ruta_perfil = models.ImageField(upload_to="Perfiles", null = True, blank = False)
    json_publicaciones = models.JSONField()
