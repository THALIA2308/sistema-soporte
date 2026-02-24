from django.conf import settings
import requests


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