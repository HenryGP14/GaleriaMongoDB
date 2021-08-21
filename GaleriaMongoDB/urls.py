from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from galeria import views as vw_galeria
from session import views as vw_session

urlpatterns = (
    [
        path("", vw_galeria.vw_index, name="index"),
        path("login/", vw_session.vw_login, name="login"),
        path("login/complete", vw_session.login, name="logear"),
        path("logout", vw_session.logout, name="logout"),
        path("create-user/", vw_session.vw_create, name="create-user"),
        path("create-publicacion/", vw_galeria.vw_create, name="create-publicacion"),
        path("delete-publicacion/", vw_galeria.vw_delete, name="delete-publicacion"),
        path("admin/", admin.site.urls),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
