from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.api import PedidoViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'itens', ItemViewSet, basename='item')


urlpatterns = [
    path('', include(router.urls)),
]