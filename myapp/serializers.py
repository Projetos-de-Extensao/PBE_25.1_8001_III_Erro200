from rest_framework import serializers
from myapp.models import Pedido, Item

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'itens', 'valor_total', 'status']
        read_only_fields = ['id']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'nome', 'descricao']
        read_only_fields = ['id']

