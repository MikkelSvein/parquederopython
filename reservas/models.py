from django.db import models
from django.conf import settings
from vehiculos.models import Vehiculo
class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField()
    confirmado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Reserva {self.id} - {self.usuario.username} - {self.vehiculo.placa}"
