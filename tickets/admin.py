from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'prioridad', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'prioridad', 'categoria')
    search_fields = ('nombre', 'correo', 'descripcion')
