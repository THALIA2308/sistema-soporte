from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_ticket, name='crear_ticket'),
    path('exito/', views.ticket_exito, name='ticket_exito'),
]
