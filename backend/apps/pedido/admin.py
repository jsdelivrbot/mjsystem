from django.contrib import admin
from django.db import models
from .models import Cliente, ClientePedido, Endereco, Pedido, Entrega
from django import forms

# class EnderecoInline(admin.StackedInline):
#     model = Endereco
#     extra = 1


class EnderecoModelForm(forms.ModelForm ):
    uf = forms.CharField()
    cep = forms.CharField()
    cidade = forms.CharField()
    endereco = forms.CharField()
    bairro = forms.CharField()
    complemento = forms.CharField()
    class Meta:
        model = Endereco
        fields = '__all__'

class ClienteAdmin(admin.ModelAdmin):
    form = EnderecoModelForm

class PedidoModelForm(forms.ModelForm ):
    obs = forms.CharField(widget=forms.Textarea )
    class Meta:
        model = Pedido
        fields = []

class PedidoInline(admin.StackedInline):
    model = Pedido
    fields = [('artigo','classe'),('quantidade', 'metragem'),('espessura','cor',),('obs'),('valor')]
    form = PedidoModelForm
    extra = 3

class EntregaAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Local De 	Entrega', {'fields': [('endereco','cep'),('cidade','bairro'),('uf', 'complemento'),('transportadora','dataentrega')]}),
    #     ]
    # inlines = [PedidoInline]
    # list_display = ('codigo',)
    pass

class ClientePedidoAdmin(admin.ModelAdmin):
    fields = [('cliente','entrega')]
    inlines = [PedidoInline]
    class Meta:
        model = Entrega
        fields = [('cep')]
    # list_display = ('codigo',)




admin.site.register(Cliente, ClienteAdmin)
# admin.site.register(Pedido)
admin.site.register(ClientePedido, ClientePedidoAdmin)
# admin.site.register(Entrega, EntregaAdmin)
