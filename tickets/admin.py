from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'edificio',
        'categoria',
        'prioridad',
        'estado',
        'fecha_creacion'
    )

    list_filter = (
        'estado',
        'prioridad',
        'categoria',
        'edificio'
    )

    search_fields = (
        'nombre',
        'correo'
    )

    def save_model(self, request, obj, form, change):
        if change:
            old_obj = Ticket.objects.get(pk=obj.pk)

            # Solo enviar correo si el estado cambió
            if old_obj.estado != obj.estado:
                send_mail(
                    subject=f"Actualización Ticket N° {obj.id}",
                    message=f"""
Estimado/a {obj.nombre},

Tu ticket N° {obj.id} ha cambiado de estado.

Nuevo estado: {obj.estado}

Edificio: {obj.edificio}
Categoría: {obj.categoria}
Prioridad: {obj.prioridad}

Saludos,
Soporte Técnico
                    """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[obj.correo],
                    fail_silently=False,
                )

        super().save_model(request, obj, form, change)