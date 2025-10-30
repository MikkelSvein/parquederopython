from django.db import models
class Tarifa(models.Model):
    bicicleta = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    bus = models.DecimalField(max_digits=10, decimal_places=2, default=5000)
    carro = models.DecimalField(max_digits=10, decimal_places=2, default=2000)
    moto = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Tarifas (actualizadas: {self.updated_at})"
