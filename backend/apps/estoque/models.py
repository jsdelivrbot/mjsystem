from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class PalletMarca(models.Model):
    pallet_origem = models.CharField(('Pallet Origem'), max_length=255)
    def __str__(self):
        return u"%s" % self.pallet_origem

@python_2_unicode_compatible   
class PalletOrigem(models.Model):
    codigo = models.ForeignKey(PalletMarca, on_delete=models.CASCADE)
    classe = models.CharField(('Classe'), max_length=15, default=None, null=True, blank=True)
    quatidade = models.CharField(('Quantidade'), max_length=255, default=None, null=True, blank=True)
    metragem = models.CharField(('Metragem'), max_length=255, default=None, null=True, blank=True)
    peso = models.CharField(('Peso'), max_length=255, default=None, null=True, blank=True)
    lote = models.CharField(('Lote'), max_length=255, default=None, null=True, blank=True)

    class Meta:
            verbose_name = (u'Pallet Origem')
            verbose_name_plural = (u'Pallet Origem')
            
    def __str__(self):
        return u"%s" % self.codigo

@python_2_unicode_compatible
class PelePele(models.Model):
    pallet = models.CharField(('Pallet'), max_length=255, default=None, null=True, blank=True)
    metragem = models.CharField(('Metragem'), max_length=255, default=None, null=True, blank=True)
    quantidade = models.CharField(('Quantidade'), max_length=255, default=None, null=True, blank=True)
    classe = models.CharField(('Classe'), max_length=255, default=None, null=True, blank=True)
    peso = models.CharField(('Peso'), max_length=255, default=None, null=True, blank=True)
    lote = models.CharField(('Lote'), max_length=255, default=None, null=True, blank=True)

    class Meta:
            verbose_name = (u'Pele a Pele')
            verbose_name_plural = (u'Pele a Pele')

    def __str__(self):
        return u"%s" % self.pallet    

@python_2_unicode_compatible
class Romaneo(models.Model):
    cliente = models.CharField(('Cliente'), max_length=255, default=None, null=True, blank=True)
    quantidade = models.CharField(('Quantidade'), max_length=255, default=None, null=True, blank=True)
    classe = models.CharField(('Classe'), max_length=255, default=None, null=True, blank=True)
    metragem = models.CharField(('Metragem'), max_length=255, default=None, null=True, blank=True)
    peso_liq = models.CharField(('Peso Liquido'), max_length=255, default=None, null=True, blank=True)
    peso_bruto = models.CharField(('Peso Bruto'), max_length=255, default=None, null=True, blank=True)
    data_saida = models.DateField()

    class Meta:
            verbose_name = (u'Romaneo')
            verbose_name_plural = (u'Romaneos')

    def __str__(self):
        return u"%s" % self.cliente
