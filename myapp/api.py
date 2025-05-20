from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from myapp.models import Pedido, Item
from myapp.serializers import ProdutoSerializer, ItemSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = ProdutoSerializer

    @action(detail=True, methods=['get'])
    def itens(self, request, pk=None):
        pedido = self.get_object()
        itens = pedido.itens.all()
        serializer = ItemSerializer(itens, many=True)
        return Response(serializer.data)
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=['get'])
    def pedidos(self, request, pk=None):
        item = self.get_object()
        pedidos = item.pedido_set.all()
        serializer = ProdutoSerializer(pedidos, many=True)
        return Response(serializer.data)