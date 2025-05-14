from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('produto/baratos/', views.produtos_baratos, name='produtos-baratos'),
    
    # Pedidos URLs
    path('pedidos/', views.meus_pedidos, name='meus-pedidos'),
    path('pedidos/novo/', views.novo_pedido, name='novo-pedido'),
    path('pedidos/gerenciar/', views.gerenciar_pedidos, name='gerenciar-pedidos'),
    path('pedidos/processar/<int:pedido_id>/', views.processar_pedido, name='processar-pedido'),
    path('pedidos/confirmar-entrega/<int:pedido_id>/', views.confirmar_entrega, name='confirmar-entrega'),
]