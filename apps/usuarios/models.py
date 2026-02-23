from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPO_USUARIO = (
        ('cliente', 'Cliente'),
        ('prestador', 'Prestador'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    horario_atendimento = models.CharField(max_length=200, blank=True, null=True)
    formas_pagamento = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

    from django.db.models.signals import post_save
    from django.dispatch import receiver

    @receiver(post_save, sender=User)
    def criar_perfil_automatico(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)
# Create your models here.
