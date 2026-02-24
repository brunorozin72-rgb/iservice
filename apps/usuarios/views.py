from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Perfil

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        tipo = request.POST.get('tipo')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe')
            return redirect('cadastro')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Perfil.objects.create(
            tipo=tipo,
            cidade=cidade,
            telefone=telefone
        )

        return redirect('home')

    return render(request, 'cadastro.html')

# Create your views here.
