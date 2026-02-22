from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Ticket
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff') 


admin.site.register(User, CustomUserAdmin)

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
        cambio_estado = False

        if change:
            old_obj = Ticket.objects.get(pk=obj.pk)
            if old_obj.estado != obj.estado:
                cambio_estado = True

        super().save_model(request, obj, form, change)

        if cambio_estado:
            try:
                subject=f"Actualización Ticket N° {obj.id}"
                message=f"""
                            Estimado/a {obj.nombre},

                            Tu ticket N° {obj.id} ha cambiado de estado.

                            Nuevo estado: {obj.estado}

                            Edificio: {obj.edificio}
                            Categoría: {obj.categoria}
                            Prioridad: {obj.prioridad}

                            Saludos,
                            Soporte Técnico"""
                
                send_mail(subject, message, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[obj.correo], fail_silently=False,)
                #messages.info(request, f"{subject}{message}")

            except Exception as e:
                print(f"Error al enviar correo: {e}")

    
