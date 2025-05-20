from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.api import PedidoViewSet, ItemViewSet, UserViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'itens', ItemViewSet, basename='item')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]