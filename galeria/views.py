from django.shortcuts import render, redirect
from django.db import transaction
from galeria.models import Publicacion
from session.models import Usuario
from django.contrib import messages
import os, time
from datetime import datetime


def vw_index(request):
    ltPublicaciones=Usuario.objects.all()
    print(ltPublicaciones)
    return render(request, "fanpague.html",{'ltPublicaciones':ltPublicaciones})


def vw_create(request):
    if request.method == "POST":
        try:
            with transaction.atomic():
                unaPublicacion = Publicacion()
                unaPublicacion.fecha = str(time.strftime("%Y-%m-%d", time.localtime()))
                unaPublicacion.direccion = request.POST["direccion"]
                unaPublicacion.descripcion = request.POST["descripcion"]
                unaPublicacion.ruta_publicacion = request.FILES["add-img"]
                a, b = os.path.splitext(unaPublicacion.ruta_publicacion.name)
                unaPublicacion.ruta_publicacion.name = "publicacion_" + str(time.strftime("%Y-%m-%d_%H::%M::%S", time.localtime())) + b
                unaPublicacion.save()
                unUsuario = Usuario.objects.get(id=request.session["usuario"]["id"])
                unUsuario.json_publicaciones.append(
                    {
                        "publicacion_id": unaPublicacion.id,
                        "fecha": unaPublicacion.fecha,
                        "direccion": unaPublicacion.direccion,
                        "descripcion": unaPublicacion.descripcion,
                        "ruta_publicacion": unaPublicacion.ruta_publicacion.url,
                    }
                )
                unUsuario.save()
                messages.success(request, "Publicación registrada exitosamente.")
                return redirect("/")
        except Exception as e:
            messages.error(request, "Existió un error al crear publicación, intentelo más tarde")
            return redirect("/")

def vw_delete(request, id):
    if request.method == "POST":
        try:
            with transaction.atomic():
                unaPublicacion = Publicacion()
                unUsuario = Usuario.objects.get(id=request.session["usuario"]["id"])
                
                messages.success(request, "Publicación eliminada exitosamente.")
                return redirect("/")
        except Exception as e:
            messages.error(request, "Existió un error al eliminar publicación, intentelo más tarde")
            return redirect("/")



