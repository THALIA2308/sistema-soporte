from django.contrib import admin
from django.urls import path
from tickets.views import crear_ticket, ticket_exito
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crear_ticket, name='crear_ticket'),
    path('exito/', ticket_exito, name='ticket_exito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])