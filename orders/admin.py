from django.contrib import admin
from .models import OrdemServico

# Register your models here.
class OrdemServicoAdmin(admin.ModelAdmin):
  list_display  = ('id', 'cliente', 'veiculo', 'status', 'criado_em')
  list_filter   = ('status',)
  search_fields = ('cliente', 'veiculo')