from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from galeria import views as vw_galeria

urlpatterns = (
    [
        path("", vw_galeria.vw_index, name="index"),
        path("admin/", admin.site.urls),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
