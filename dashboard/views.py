from django.shortcuts import render
from vehiculos.models import Vehiculo
from reservas.models import Reserva
def panel(request):
    total = Vehiculo.objects.count()
    reservas = Reserva.objects.filter(confirmado=False).count()
    # placeholder for available slots, assume 100 capacity
    capacidad = 100
    disponibles = capacidad - total
    return render(request, 'dashboard/panel.html', {'total':total,'reservas':reservas,'disponibles':disponibles})
