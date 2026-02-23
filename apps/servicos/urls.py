from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servico/<int:id>/', views.detalhe_servico, name='detalhe_servico'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('criar-servico/', views.criar_servico, name='criar_servico'),
    path('editar-servico/<int:id>/', views.editar_servico, name='editar_servico'),
    path('excluir-servico/<int:id>/', views.excluir_servico, name='excluir_servico'),
    path('contato/<int:id>/', views.contato_prestador, name='contato_prestador'),
]

