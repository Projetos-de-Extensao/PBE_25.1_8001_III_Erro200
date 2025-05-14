from django.contrib import admin
from .models import Produto, Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'status', 'data_criacao']
    list_filter = ['status', 'data_criacao']
    search_fields = ['usuario__username']
    inlines = [ItemPedidoInline]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'disponivel']
    list_filter = ['disponivel']
    search_fields = ['nome']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)