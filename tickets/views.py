import requests
from django.shortcuts import render, redirect
from django.conf import settings
from tickets.utils import enviar_a_n8n
from .forms import TicketForm


def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            print(ticket)
            enviar_a_n8n(ticket)

            return redirect('ticket_exito')
    else:
        form = TicketForm()

    return render(request, 'crear_ticket.html', {'form': form})


def ticket_exito(request):
    return render(request, 'ticket_exito.html')