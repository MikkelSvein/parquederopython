from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_cliente = True
            user.save()
            messages.success(request, 'Usuario registrado')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('vehiculos_lista')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
