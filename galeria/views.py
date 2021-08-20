from django.shortcuts import render
from django.db import transaction
from galeria.models import Publicacion
from session.models import Usuario
from datetime import datetime
import os


def vw_index(request):
    return render(request, "fanpague.html")

def vw_create(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                unaPublicacion = Publicacion()
                unaPublicacion.direccion = request.POST['direccion']
                unaPublicacion.descripcion = request.POST['descripcion']
                unaPublicacion.ruta_publicacion = request.FILES['add-img']
                a,b = os.path.splitext(unaPublicacion.ruta_publicacion.name)
                unaPublicacion.ruta_publicacion.name="publicacion_" + str(datetime.now().year) + "-" + str(datetime.now().month)+ "-" + str(datetime.now().day) + b
                unaPublicacion.save()

                unUsuario = Usuario.objects.get(id = 18)
                unUsuario.json_publicaciones.append({"publicacion_id": unaPublicacion.id, "direccion": unaPublicacion.direccion, "descripcion": unaPublicacion.descripcion, "ruta_foto": unaPublicacion.ruta_publicacion.url})
                unUsuario.save()
                return render(request, "fanpague.html", {"sms": "Publicación registrada exitosamente."})
        except Exception as e:
            return render(request, "fanpague.html", {"sms": "Existió un error al crear publicación."})

