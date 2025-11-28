from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.db import IntegrityError
from django.db.models import Q
from .models import *

# Create your views here.

## Ordem de Serviço Views
class OrdemListView(ListView):
  model = OrdemServico
  template_name = 'orders/ordem_list.html'
  context_object_name = 'ordens'
  ordering = ['-criado_em']
  paginate_by         = 5

  def get_queryset(self):
    queryset = super().get_queryset()

    search   = self.request.GET.get('search')

    if search:
      queryset = queryset.filter(
        Q(descricao__contains = search)       |
        Q(cliente__nome__contains = search)   |
        Q(veiculo__modelo__contains = search) |
        Q(veiculo__placa__contains = search)  |
        Q(veiculo__modelo__contains = search) |
        Q(status__descricao__contains = search) 
      )

    return queryset

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
  paginate_by         = 5

  def get_queryset(self):
    queryset = super().get_queryset()

    search   = self.request.GET.get('search')

    if search:
      queryset = queryset.filter(
        Q(nome__contains = search) |
        Q(email__contains = search)
      )

    return queryset

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
  
#Veiculos Views
class VeiculoListView(ListView):
  model               = Veiculo
  template_name       = 'orders/veiculos_list.html'
  context_object_name = 'veiculos'
  ordering            = ['-criado_em']
  paginate_by         = 5

  def get_queryset(self):
    queryset = super().get_queryset()

    search   = self.request.GET.get('search')

    if search:
      queryset = queryset.filter(
        Q(placa__contains = search)  |
        Q(modelo__contains = search) |
        Q(ano__contains = search)    |
        Q(cliente__nome__contains = search)
      )

    return queryset

def veiculoClienteView(request, cliente_pk):
  veiculos      = Veiculo.objects.filter(cliente_id=cliente_pk).values('id', 'modelo', 'placa')
  veiculos_list = list(veiculos)
  return JsonResponse(veiculos_list, safe=False)

class VeiculoCreateView(CreateView):
  model         = Veiculo
  fields        = ['cliente', 'marca', 'modelo', 'ano', 'placa'] 
  template_name = 'orders/veiculos_form.html'
  success_url   = reverse_lazy('veiculo-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = False
    return context

class VeiculoUpdateView(UpdateView):
  model         = Veiculo
  fields        = ['cliente', 'marca', 'modelo', 'ano', 'placa']
  template_name = 'orders/veiculos_form.html'
  success_url   = reverse_lazy('veiculo-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = True
    return context
  
class VeiculoDeleteView(UpdateView):
  def post(self, request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    veiculo.delete()
    return redirect('veiculo-list')
  
## Mecânicos Views
class MecanicoListView(ListView):
  model               = Mecanico
  template_name       = 'orders/mecanicos_list.html'
  context_object_name = 'mecanicos'
  ordering            = ['-criado_em']
  paginate_by         = 5

  def get_queryset(self):
    queryset = super().get_queryset()

    search   = self.request.GET.get('search')

    if search:
      queryset = queryset.filter(
        Q(nome__contains = search) |
        Q(email__contains = search)
      )

    return queryset
  
class MecanicoCreateView(CreateView):
  model         = Mecanico
  fields        = ['nome', 'email']
  template_name = 'orders/mecanicos_form.html'
  success_url   = reverse_lazy('mecanico-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = False
    return context  
  
class MecanicoUpdateView(UpdateView):
  model         = Mecanico
  fields        = ['nome', 'email']
  template_name = 'orders/mecanicos_form.html'
  success_url   = reverse_lazy('mecanico-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = True
    return context
  
class MecanicoDeleteView(UpdateView):
  def post(self, request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    mecanico.delete()
    return redirect('mecanico-list')
  
## Status Views
class StatusListView(ListView):
  model               = Status
  template_name       = 'orders/status_list.html'
  context_object_name = 'status_list'
  ordering            = ['-criado_em']
  paginate_by         = 5

  def get_queryset(self):
    queryset = super().get_queryset()

    search   = self.request.GET.get('search')

    if search:
      queryset = queryset.filter(
        Q(descricao__contains = search) |
        Q(cor__contains = search)
      )

    return queryset

class StatusCreateView(CreateView):
  model         = Status
  fields        = ['descricao', 'cor']
  template_name = 'orders/status_form.html'
  success_url   = reverse_lazy('status-list')
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = False 
    return context
  
class StatusUpdateView(UpdateView):
  model         = Status
  fields        = ['descricao', 'cor']
  template_name = 'orders/status_form.html'
  success_url   = reverse_lazy('status-list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['is_edit'] = True
    return context
  
class StatusDeleteView(UpdateView):
  def post(self, request, pk):
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return redirect('status-list')
  
## Responsável OS View
class ResponsavelListView(ListView):
  model               = ResponsavelOS
  template_name       = 'orders/responsavel_list.html'
  context_object_name = 'responsaveis'
  paginate_by         = 5

  def get_queryset(self):
    self.ordem_servico = get_object_or_404(
        OrdemServico, 
        pk=self.kwargs['ordem_id']
    )

    queryset = (
        ResponsavelOS.objects
        .filter(ordem_servico=self.ordem_servico)
        .select_related('mecanico')
    )

    search = self.request.GET.get('search')

    if search:
        queryset = queryset.filter(
            Q(mecanico__nome__icontains=search)
        )

    return queryset

  # def get_queryset(self):
  #   self.ordem_servico = get_object_or_404(OrdemServico, pk=self.kwargs['ordem_id'])
  #   return ResponsavelOS.objects.filter(ordem_servico=self.ordem_servico).select_related('mecanico')
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['ordem_servico'] = self.ordem_servico
    return context
  
  
class ResponsavelCreateView(CreateView):
  model         = ResponsavelOS
  fields        = ['mecanico']
  template_name = 'orders/responsavel_form.html'

  def get_success_url(self):
    return reverse_lazy('responsavel-list', kwargs={'ordem_id': self.kwargs['ordem_id']})
  
  def form_valid(self, form):
    form.instance.ordem_servico = get_object_or_404(OrdemServico, pk=self.kwargs['ordem_id'])
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['ordem_servico']   = get_object_or_404(OrdemServico, pk=self.kwargs['ordem_id'])
    context['is_edit'] = False

    return context
  
class ResponsavelUpdateView(UpdateView):
  model         = ResponsavelOS
  fields        = ['mecanico']
  template_name = 'orders/responsavel_form.html'

  def get_queryset(self):
    ordem = get_object_or_404(OrdemServico, pk=self.kwargs['ordem_id'])
    return ResponsavelOS.objects.filter(ordem_servico=ordem)
  
  def get_success_url(self):
    return reverse_lazy('responsavel-list', kwargs={'ordem_id': self.kwargs['ordem_id']})

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['ordem_servico'] = get_object_or_404(OrdemServico, pk=self.kwargs['ordem_id'])
    context['is_edit'] = True
    return context
  
  def form_valid(self, form):
    try:
      return super().form_valid(form)
    except IntegrityError:
      form.add_error('mecanico', 'Este mecânico já está vinculado a esta OS.')
      return self.form_invalid(form)
    
class ResponsavelDeleteView(View):
    def post(self, request, ordem_id, pk):
      responsavel = get_object_or_404(ResponsavelOS, pk=pk, ordem_servico_id= ordem_id)
      responsavel.delete()
      return redirect('responsavel-list', ordem_id=ordem_id)