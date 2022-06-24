from django.db import models

# Model de usuarios

class Usuarios(models.Model):
  # Dados pessoais
  nome = models.CharField(max_length=250, null=True, blank=False, verbose_name="Nome")
  email = models.EmailField(verbose_name = "E-mail")
  # Endereço do usuário
  pais = models.CharField(max_length=250, null=True, blank=False, verbose_name="País")
  cep = models.CharField(max_length=9,null=True, blank=False, verbose_name = "CEP")
  uf_endereco = models.CharField(max_length=50, null=True, blank=False, verbose_name="Estado")
  cidade = models.CharField(max_length=75, null=True, blank=False, verbose_name="Município")
  rua = models.CharField(max_length=60, null=True, blank=False, verbose_name="Logradouro")
  casa = models.CharField(max_length=5, null=True, blank=False, verbose_name = "Número")
  complemento_endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name = "Complemento")
  # Dados que serão usados para autenticar
  cpf = models.CharField(max_length=16,null=True, blank=False, verbose_name = "CPF")
  numero_pis = models.CharField(max_length=11 ,null=True, blank=False, verbose_name = "Número do PIS")
  senha = models.CharField(max_length=30, null=True, blank=False, verbose_name = "Senha")
  class Meta:
    db_table = "usuarios"
    
  def __str__(self):
    return self.nome