from django.urls import path
from . import views

urlpatterns = [
  # Ordem de Serviço URLs
  path('', views.OrdemListView.as_view(), name='ordem-list'),
  path('new/', views.OrdemCreateView.as_view(), name='ordem-create'),
  path('editar/<uuid:pk>/', views.OrdemUpdateView.as_view(), name='ordem-edit'),
  path('excluir/<uuid:pk>/', views.OrdemDeleteView.as_view(), name='ordem-delete'),
  # Cliente URLs
  path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
  path('clientes/new/', views.ClienteCreateView.as_view(), name='cliente-create'),
  path('clientes/editar/<uuid:pk>/', views.ClienteUpdateView.as_view(), name='cliente-edit'),
  path('clientes/excluir/<uuid:pk>/', views.ClienteDeleteView.as_view(), name='cliente-delete'),
  # Veiculo URLs
  path('veiculos/', views.VeiculoListView.as_view(), name='veiculo-list'),
  path('veiculos/new/', views.VeiculoCreateView.as_view(), name='veiculo-create'),
  path('veiculos/editar/<uuid:pk>/', views.VeiculoUpdateView.as_view(), name='veiculo-edit'),
  path('veiculos/excluir/<uuid:pk>/', views.VeiculoDeleteView.as_view(), name='veiculo-delete'),
]