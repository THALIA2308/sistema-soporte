from django.shortcuts import render, redirect
from .forms import TicketForm


def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_exito')
    else:
        form = TicketForm()

    return render(request, 'crear_ticket.html', {'form': form})


def ticket_exito(request):
    return render(request, 'ticket_exito.html')
