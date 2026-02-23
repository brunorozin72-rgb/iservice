from django.shortcuts import render, get_object_or_404
from .models import Servico

def home(request):
    servicos = Servico.objects.all()

    nome = request.GET.get('nome')
    categoria = request.GET.get('categoria')
    cidade = request.GET.get('cidade')

    if nome:
        servicos = servicos.filter(nome__icontains=nome)

    if categoria:
        servicos = servicos.filter(categoria__icontains=categoria)

    if cidade:
        servicos = servicos.filter(cidade__icontains=cidade)

    return render(request, 'home.html', {
        'servicos': servicos,
        'nome': nome or '',
        'categoria': categoria or '',
        'cidade': cidade or '',
    })

from django.shortcuts import get_object_or_404

def detalhe_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    return render(request, 'detalhe_servico.html', {'servico': servico})

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from apps.usuarios.models import Perfil

@login_required
def criar_servico(request):
    perfil = Perfil.objects.get(user=request.user)

    if perfil.tipo != 'prestador':
        return redirect('home')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        cidade = request.POST.get('cidade')

        Servico.objects.create(
            nome=nome,
            descricao=descricao,
            categoria=categoria,
            cidade=cidade,
            usuario=request.user
        )

        return redirect('dashboard')

    return render(request, 'criar_servico.html')

@login_required
def dashboard(request):
    perfil = Perfil.objects.get(user=request.user)

    if perfil.tipo == 'prestador':
        servicos = Servico.objects.filter(usuario=request.user)
    else:
        servicos = None

    return render(request, 'dashboard.html', {
        'perfil': perfil,
        'servicos': servicos
    })
@login_required
def excluir_servico(request, id):
    servico = get_object_or_404(Servico, id=id, usuario=request.user)
    servico.delete()
    return redirect('dashboard')

@login_required
def editar_servico(request, id):
    servico = get_object_or_404(Servico, id=id, usuario=request.user)

    if request.method == 'POST':
        servico.nome = request.POST.get('nome')
        servico.descricao = request.POST.get('descricao')
        servico.categoria = request.POST.get('categoria')
        servico.cidade = request.POST.get('cidade')
        servico.save()
        return redirect('dashboard')

    return render(request, 'editar_servico.html', {'servico': servico})

from django.contrib.auth.decorators import login_required

@login_required
def contato_prestador(request, id):
    servico = get_object_or_404(Servico, id=id)
    perfil = servico.usuario.perfil

    return render(request, 'contato_prestador.html', {
        'servico': servico,
        'perfil': perfil
    })


# Create your views here.
