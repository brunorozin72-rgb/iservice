from django.db import models
from django.contrib.auth.models import User

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    cidade = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

from django.contrib.auth.models import User


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('negociacao', 'Em negociação'),
        ('aceito', 'Aceito'),
        ('encerrado', 'Encerrado'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos_feitos')
    prestador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos_recebidos')
    servico = models.ForeignKey('Servico', on_delete=models.CASCADE)
    descricao = models.TextField()
    material_desejado = models.TextField(blank=True, null=True)
    orcamento_estimado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.username} → {self.prestador.username}'


class Proposta(models.Model):
    STATUS_CHOICES = [
        ('enviada', 'Enviada'),
        ('aceita', 'Aceita'),
        ('recusada', 'Recusada'),
    ]

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='propostas')
    versao = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    prazo = models.CharField(max_length=100)
    materiais_inclusos = models.BooleanField(default=False)
    observacoes = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enviada')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Proposta v{self.versao} - Pedido #{self.pedido.id}'
# Create your models here.
