from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('APXX/', admin.site.urls),
    path('auth/', include("login_register.urls")),
    path('', include("Panel.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)