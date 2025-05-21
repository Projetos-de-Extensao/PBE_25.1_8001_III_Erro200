from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.api import PedidoViewSet, ItemViewSet, UserViewSet, PortoViewSet, PostoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'itens', ItemViewSet, basename='item')
router.register(r'users', UserViewSet, basename='user')
router.register(r'portos', PortoViewSet, basename='porto')
router.register(r'postos', PostoViewSet, basename='posto')


urlpatterns = [
    path('', include(router.urls)),
]