from django.shortcuts import render, redirect
from .models import Tarifa
from .forms import TarifaForm
def ver_tarifas(request):
    t = Tarifa.objects.first()
    return render(request, 'tarifas/ver.html', {'t':t})
def editar_tarifas(request):
    t = Tarifa.objects.first()
    if not t:
        t = Tarifa.objects.create()
    if request.method == 'POST':
        form = TarifaForm(request.POST, instance=t)
        if form.is_valid():
            form.save()
            return redirect('ver_tarifas')
    else:
        form = TarifaForm(instance=t)
    return render(request, 'tarifas/editar.html', {'form':form})
