from django.db import models
from django.utils import timezone
from datetime import date
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Cliente(models.Model):
    nome = models.CharField(('NOME'), max_length=255)
    razao_social = models.CharField(('RAZÃO SOCIAL'), max_length=255, default=None, blank=True )
    cnpj = models.CharField(('CNPJ'), max_length=15, default=None, null=True, blank=True)
    fone = models.CharField(('FONE'), max_length=10, default=None, null=True, blank=True) 
    email = models.EmailField(('E-MAIL'), max_length=20, default=None, null=True, blank=True)
    def __str__(self):
        return u"%s" % self.nome

@python_2_unicode_compatible 
class Entrega(models.Model):
    dataentrega = models.DateField(('Data Entrega'), default=date.today, null=True)
    endereco = models.CharField(('Endereço'), max_length=255, default=None, blank=True)
    cep = models.CharField(('CEP'), max_length=8, default=None, null=True, blank=True)
    cidade = models.CharField(('Cidade'), max_length=255, default=None, null=True, blank=True)
    bairro = models.CharField(('Bairro'), max_length=255, default=None, )
    complemento = models.CharField(('Complemento'), max_length=255, blank=True)
    uf = models.CharField(('UF'), max_length=255, default=None, null=True, blank=True)
    transportadora = models.CharField(('Transportadora'), max_length=255, blank=True)

    class Meta:
            verbose_name = (u'Entrega')
            verbose_name_plural = (u'Entregas')

@python_2_unicode_compatible
class ClientePedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE)

@python_2_unicode_compatible
class Endereco(models.Model):   
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    uf = models.CharField(('UF'), max_length=255, default=None, null=True, blank=True)
    cep = models.CharField(('CEP'), max_length=8, default=None, null=True, blank=True)
    cidade = models.CharField(('Cidade'), max_length=255, default=None, null=True, blank=True)
    endereco = models.CharField(('Endereço'), max_length=255, default=None, blank=True)
    bairro = models.CharField(('Bairro'), max_length=255, default=None, blank=True )
    complemento = models.CharField(('Complemento'), max_length=255, blank=True)




    def __str__(self):
        return u"%s" % self.endereco

@python_2_unicode_compatible   
class Pedido(models.Model):
    cliente = models.ForeignKey(ClientePedido, on_delete=models.CASCADE)
    quantidade = models.DecimalField(('Quantidade'), max_digits=20, decimal_places=2, default=0, null=True, blank=True)
    classe = models.CharField(('Classe'), max_length=15, default=None, null=True, blank=True)
    artigo = models.CharField(('Artigo'), max_length=15, default=None, null=True, blank=True)
    metragem = models.DecimalField(('Metragem'), max_digits=8, decimal_places=2, default=0, null=True, blank=True)
    espessura = models.DecimalField(('Espessura'), max_digits=20, decimal_places=2, default=0, null=True, blank=True)
    cor = models.CharField(('Cor'), max_length=15, default=None, null=True, blank=True)
    obs = models.CharField(('Observações'), max_length=255, default=None, null=True, blank=True)
    valor = models.DecimalField(('Valor'), max_digits=8, decimal_places=2, default=0)

    # class Meta:
    #         verbose_name = (u'Pedido')
    #         verbose_name_plural = (u'Pedidos')
            
    # def __str__(self):
    #     return u"%s" % self.codigo
