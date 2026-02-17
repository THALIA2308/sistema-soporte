from django.contrib import admin
from django.urls import path
from tickets.views import crear_ticket, ticket_exito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crear_ticket, name='crear_ticket'),
    path('exito/', ticket_exito, name='ticket_exito'),
]
