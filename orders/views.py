from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import OrdemServico

# Create your views here.
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

class OrdemUpdateView(UpdateView):
  model = OrdemServico
  fields = ['cliente', 'veiculo', 'descricao', 'status']
  template_name = 'orders/ordem_form.html'
  success_url = reverse_lazy('ordem-list')