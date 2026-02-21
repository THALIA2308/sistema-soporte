from django.db import models



class Ticket(models.Model):
    

    CARGO_CHOICES = [
        ('Conserje', 'Conserje'),
        ('Administrador', 'Administrador'),
    ]

    CATEGORIA_CHOICES = [
        ('Agregar usuario', 'Agregar usuario'),
        ('Eliminar usuario', 'Eliminar usuario'),
        ('Soporte técnico', 'Soporte técnico'),
        ('Solicitud de capacitación', 'Solicitud de capacitación'),
        ('Otra', 'Otra'),
    ]

    PRIORIDAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    ESTADO_CHOICES = [
        ('Recibido', 'Recibido'),
        ('En revisión', 'En revisión'),
        ('En proceso', 'En proceso'),
        ('En espera de información', 'En espera de información'),
        ('Cerrado', 'Cerrado'),
    ]

    # Datos solicitante
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    correo = models.EmailField()
    edificio = models.CharField(max_length=200)

    # Datos ticket
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    tipo_accion = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=30,
        choices=ESTADO_CHOICES,
        default='Recibido'
    )
    
    def __str__(self):
        return f"Ticket #{self.id} - {self.nombre}"
