from django.db import models

# Create your models here.
from django.db import models
import uuid

class Status(models.Model):
  id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  descricao     = models.CharField(max_length=50, unique=True)
  cor           = models.CharField(max_length=7)  # 7 digitos pois a cor precisa ser em formato hexadecimal
  criado_em     = models.DateTimeField(auto_now_add=True)
  atualizado_em = models.DateTimeField(auto_now=True)

class OrdemServico(models.Model):
  id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  cliente    = models.ForeignKey('Cliente', on_delete=models.CASCADE)
  veiculo    = models.ForeignKey('Veiculo', on_delete=models.CASCADE)
  descricao  = models.TextField(blank=True)
  status     = models.ForeignKey('Status', on_delete=models.CASCADE)
  criado_em  = models.DateTimeField(auto_now_add=True)
  atualizado_em = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.cliente} - {self.status}"
  
class Cliente(models.Model):
  id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  nome          = models.CharField(max_length=100)
  email         = models.EmailField(unique=True)
  criado_em     = models.DateTimeField(auto_now_add=True)
  atualizado_em = models.DateTimeField(auto_now=True)

class Veiculo(models.Model):
  id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  cliente       = models.ForeignKey('Cliente', on_delete=models.CASCADE)
  marca         = models.CharField(max_length=50)
  modelo        = models.CharField(max_length=50)
  ano           = models.PositiveIntegerField()
  placa         = models.CharField(max_length=20, unique=True)
  criado_em     = models.DateTimeField(auto_now_add=True)
  atualizado_em = models.DateTimeField(auto_now=True)

class ResponsavelOS(models.Model):
  id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  ordem_servico = models.ForeignKey('OrdemServico', on_delete=models.CASCADE)
  mecanico      = models.ForeignKey('Mecanico', on_delete=models.CASCADE)
  atribuido_em  = models.DateTimeField(auto_now_add=True)
  
class Mecanico(models.Model):
  id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  nome          = models.CharField(max_length=100)
  email         = models.EmailField(unique=True)
  criado_em     = models.DateTimeField(auto_now_add=True)
  atualizado_em = models.DateTimeField(auto_now=True)