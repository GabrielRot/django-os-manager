from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from .models import *

# Create your views here.

## Ordem de Serviço Views
class OrdemListView(ListView):
  model = OrdemServico
  template_name = 'orders/ordem_list.html'
  context_object_name = 'ordens'
  ordering = ['-criado_em']

class OrdemCreateView(CreateView):
  model = OrdemServico
  fields = ['cliente', 'veiculo', 'descricao', 'status']
  template_name = 'orders/ordem_form.html'
  success_url = reverse_lazy('ordem-list')

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    context['is_edit'] = False
    return context

class OrdemUpdateView(UpdateView):
  model = OrdemServico
  fields = ['cliente', 'veiculo', 'descricao', 'status']
  template_name = 'orders/ordem_form.html'
  success_url = reverse_lazy('ordem-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = True
    return context
  
class OrdemDeleteView(UpdateView):
  def post(self, request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    ordem.delete()
    return redirect('ordem-list')
  
## Cliente Views

class ClienteListView(ListView):
  model               = Cliente
  template_name       = 'orders/clientes_list.html'
  context_object_name = 'clientes'
  ordering            = ['-criado_em']

class ClienteCreateView(CreateView):
  model         = Cliente
  fields        = ['nome', 'email']
  template_name = 'orders/clientes_form.html'
  success_url   = reverse_lazy('cliente-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = False
    return context
  
class ClienteUpdateView(UpdateView):
  model         = Cliente
  fields        = ['nome', 'email']
  template_name = 'orders/clientes_form.html'
  success_url   = reverse_lazy('cliente-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = True
    return context
  
class ClienteDeleteView(UpdateView):
  def post(self, request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('cliente-list')