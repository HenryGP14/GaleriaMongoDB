from djongo import models
from fernet_fields import EncryptedTextField

class Usuario(models.Model):
    nombres = models.CharField(max_length = 60, null = False, blank = True)
    nomusuario = models.CharField(max_length = 25, null = False, blank = True)
    contrasenia = EncryptedTextField()
    json_publicaciones = models.JSONField(null = True, blank = False)
