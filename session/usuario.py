class Session:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        usuario = self.session.get("usuario")
        if not usuario:
            usuario = self.session["usuario"] = {}
        self.usuario = usuario

    def add(self, usuario):
        self.usuario = {
            "id": usuario.id,
            "nombre": usuario.nombres,
            "autorizado": True,
        }
        self.save()

    def save(self):
        self.session["usuario"] = self.usuario
        self.session.modified = True

    def clear(self):
        self.session["usuario"] = {}
        self.session.modified = True
