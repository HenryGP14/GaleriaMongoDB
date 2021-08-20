from djongo import models
from fernet_fields import EncryptedTextField

class Usuario(models.Model):
    nombres = models.CharField(max_length = 60, null = False, blank = True)
    nomusuario = models.CharField(max_length = 25, null = False, blank = True)
    contrasenia = EncryptedTextField()
    ruta_perfil = models.ImageField(upload_to="Perfiles", null = True, blank = False)
    json_publicaciones = models.JSONField()
