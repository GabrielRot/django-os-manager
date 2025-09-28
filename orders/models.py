from django.db import models

# Create your models here.
from django.db import models
import uuid

class OrdemServico(models.Model):
  STATUS_PENDENTE  = 'PENDENTE'
  STATUS_ANDAMENTO = 'ANDAMENTO'
  STATUS_IMPEDIDO  = 'IMPEDIDO'
  STATUS_ARQUIVADO = 'ARQUIVADO'
  STATUS_CONCLUIDO = 'CONCLUIDO'
  STATUS_CHOICES = [
    (STATUS_PENDENTE, 'Pendente'),
    (STATUS_ANDAMENTO, 'Em Andamento'),
    (STATUS_IMPEDIDO, 'Impedido'),
    (STATUS_ARQUIVADO, 'Arquivado'),
    (STATUS_CONCLUIDO, 'Concluído'),
  ]

  id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  cliente    = models.CharField(max_length=100)
  veiculo    = models.CharField(max_length=100, blank=True)
  descricao  = models.TextField(blank=True)
  status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDENTE)
  criado_em  = models.DateTimeField(auto_now_add=True)
  atualizado_em = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.cliente} - {self.status}"