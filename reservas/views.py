from django.shortcuts import render, redirect
from .forms import ReservaForm
from .models import Reserva
from django.contrib.auth.decorators import login_required
@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by('-created_at')
    return render(request, 'reservas/mis_reservas.html', {'reservas':reservas})
@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.usuario = request.user
            r.save()
            return redirect('mis_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear.html', {'form':form})
