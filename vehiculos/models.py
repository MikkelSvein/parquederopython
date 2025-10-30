from django.db import models

class Vehiculo(models.Model):
    TIPO_CHOICES = [
        ('Bicicleta', 'Bicicleta'),
        ('Moto', 'Moto'),
        ('Carro', 'Carro'),
        ('Bus', 'Bus'),
    ]
    placa = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.placa} - {self.tipo}"
