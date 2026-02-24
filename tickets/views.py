import requests
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import TicketForm
from .models import Ticket


def enviar_a_n8n(ticket):
    try:
        payload = {
            "id": ticket.id,
            "edificio": ticket.edificio,
            "nombre": ticket.nombre,
            "cargo": ticket.cargo,
            "estado": ticket.estado,
            "correo": ticket.correo,
            "categoria": ticket.categoria,
        }

        response = requests.post(
            settings.N8N_WEBHOOK_URL,
            json=payload,
            timeout=10
        )

        response.raise_for_status()

    except Exception as e:
        print("Error enviando a n8n:", e)

def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            print(ticket)
            enviar_a_n8n(ticket)

            mensaje = f"""
Nuevo Ticket N° {ticket.id}

Edificio: {ticket.edificio}
Nombre: {ticket.nombre}
Cargo: {ticket.cargo}
Correo: {ticket.correo}

Categoría: {ticket.categoria}
Descripción:
{ticket.descripcion}

Prioridad: {ticket.prioridad}
Estado: {ticket.estado}
Fecha: {ticket.fecha_creacion}
            """

            # Enviar correo a cliente + empresa
           # send_mail(
            #    subject=f"Nuevo Ticket N° {ticket.id}",
             #   message=mensaje,
              #  from_email=settings.EMAIL_HOST_USER,
               # recipient_list=[
                #    ticket.correo,        # quien envía el ticket
                 #   "soporte@axede.cl",   # correo empresa
               # ],
                #fail_silently=False,
            #)

            return redirect('ticket_exito')
    else:
        form = TicketForm()

    return render(request, 'crear_ticket.html', {'form': form})


def ticket_exito(request):
    return render(request, 'ticket_exito.html')