from django.shortcuts import render
from session.models import Usuario

def vw_login(request):
    return render(request, "session.html")


def vw_create(request):
    if request.method == 'POST':
        try:
            unUsuario = Usuario()
            unUsuario.nombres = request.POST['nombres']
            unUsuario.nomusuario = request.POST['usuario']
            unUsuario.contrasenia = request.POST['credenciales']
            unUsuario.save()
            return render(request, "session.html", {"user_create": "Usuario registrado correctamente"})
        except Exception as e:
            return render(request, "session.html", {"sms_error": str(e)})        
            #return render(request, "session.html", {"sms_error": "Existió un error al crear el usuario"})        
    