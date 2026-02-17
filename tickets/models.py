from django.db import models


class Ticket(models.Model):

    # ---- OPCIONES ----

    CARGO_OPCIONES = [
        ('Conserje', 'Conserje'),
        ('Administrador', 'Administrador'),
    ]

    CATEGORIA_OPCIONES = [
        ('Agregar usuario', 'Agregar usuario'),
        ('Eliminar usuario', 'Eliminar usuario'),
        ('Soporte técnico', 'Soporte técnico'),
        ('Solicitud de capacitación', 'Solicitud de capacitación'),
        ('Otra', 'Otra'),
    ]

    PRIORIDAD_OPCIONES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    ESTADO_OPCIONES = [
        ('Recibido', 'Recibido'),
        ('En revisión', 'En revisión'),
        ('En proceso', 'En proceso'),
        ('En espera de información', 'En espera de información'),
        ('Cerrado', 'Cerrado'),
    ]

    # ---- DATOS DEL SOLICITANTE ----

    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=20, choices=CARGO_OPCIONES)
    correo = models.EmailField()

    # ---- DATOS DEL TICKET ----

    categoria = models.CharField(max_length=50, choices=CATEGORIA_OPCIONES)
    tipo_accion = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_OPCIONES)

    estado = models.CharField(
        max_length=30,
        choices=ESTADO_OPCIONES,
        default='Recibido'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.nombre} - {self.estado}"
