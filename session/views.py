from django.shortcuts import render, redirect
from django.contrib import messages
from session.models import Usuario

from session.usuario import Session
from session.models import Usuario


def vw_login(request):
    user_session = Session(request)
    try:
        if request.session["usuario"]:
            return redirect("/")
    except:
        pass
    return render(request, "session.html")


def login(request):
    user_session = Session(request)
    try:
        if request.session["usuario"]:
            return redirect("login")
    except:
        pass
    try:
        user = Usuario.objects.get(nomusuario=request.POST["usuario"])
    except:
        return redirect("login")

    if user.contrasenia == request.POST["credenciales"]:
        user_session.add(user)
        return redirect("/")

    else:
        return redirect("login")


def logout(request):
    user_session = Session(request)
    try:
        if not request.session["usuario"]:
            return redirect("login")
    except:
        pass
    user_session.clear()
    return redirect("/")


def vw_create(request):
    if request.method == "POST":
        user_session = Session(request)
        try:
            if request.session["usuario"]:
                return redirect("/")
        except:
            pass
        try:
            # unUsuario = Usuario()
            # unUsuario.nombres = request.POST["nombres"]
            # unUsuario.nomusuario = request.POST["usuario"]
            # unUsuario.contrasenia = request.POST["credenciales"]
            # unUsuario.json_publicaciones = []
            # unUsuario.save()
            messages.success(request, "Usuario registrado correctamente.")
            return redirect("/")
        except Exception as e:
            messages.error(request, "Existió un error al crear el usuario.")
            return redirect("/")
