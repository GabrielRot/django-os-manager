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
  path('veiculos/cliente/<uuid:cliente_pk>/', views.veiculoClienteView, name="veiculo-cliente"),
  # Mecânico URLs
  path('mecanicos/', views.MecanicoListView.as_view(), name='mecanico-list'),
  path('mecanicos/new/', views.MecanicoCreateView.as_view(), name='mecanico-create'),
  path('mecanicos/editar/<uuid:pk>/', views.MecanicoUpdateView.as_view(), name='mecanico-edit'),
  path('mecanicos/excluir/<uuid:pk>/', views.MecanicoDeleteView.as_view(), name='mecanico-delete'),
  # Status URLs
  path('status/', views.StatusListView.as_view(), name='status-list'),
  path('status/new/', views.StatusCreateView.as_view(), name='status-create'),
  path('status/editar/<uuid:pk>/', views.StatusUpdateView.as_view(), name='status-edit'),
  path('status/excluir/<uuid:pk>/', views.StatusDeleteView.as_view(), name='status-delete'),
  # Responsável OS URLs
  path('ordens/<uuid:ordem_id>/responsaveis/', views.ResponsavelListView.as_view(), name='responsavel-list'), 
  path('ordens/<uuid:ordem_id>/responsaveis/new/', views.ResponsavelCreateView.as_view(), name='responsavel-create'),
  path('ordens/<uuid:ordem_id>/responsaveis/<uuid:pk>/editar/', views.ResponsavelUpdateView.as_view(), name='responsavel-edit'),
  path('ordens/<uuid:ordem_id>/responsaveis/<uuid:pk>/excluir/', views.ResponsavelDeleteView.as_view(), name='responsavel-delete')
]