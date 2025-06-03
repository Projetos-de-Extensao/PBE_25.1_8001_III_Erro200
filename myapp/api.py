from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pedido, Porto, Posto, UserProfile
from .serializers import PedidoSerializer, UserProfileSerializer, PortoSerializer, PostoSerializer
from django.contrib.auth.models import User
from rest_framework import permissions

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Pedido.objects.all()
        
        try:
            user_profile = UserProfile.objects.get(user=user)
            
            if user_profile.user_type == 'MORADOR':
                # Morador vê apenas seus próprios pedidos
                return Pedido.objects.filter(cliente=user).order_by('-created_at')
            elif user_profile.user_type == 'ENTREGADOR':
                # Entregador vê pedidos disponíveis e seus aceitos
                return (
                    Pedido.objects.filter(status='A_CONFIRMAR') |
                    Pedido.objects.filter(entregador=user, status__in=['ACEITO', 'EM_TRANSITO', 'NO_PORTO'])
                ).order_by('-created_at')
            elif user_profile.user_type == 'BARQUEIRO':
                # Barqueiro vê pedidos no porto e seus aceitos
                return (
                    Pedido.objects.filter(status='NO_PORTO') |
                    Pedido.objects.filter(barqueiro=user, status__in=['EM_TRAVESSIA', 'NO_POSTO'])
                ).order_by('-created_at')
            elif user_profile.user_type == 'ADMIN':
                return Pedido.objects.all()
        except UserProfile.DoesNotExist:
            return Pedido.objects.none()
            
        return Pedido.objects.none()

    @action(detail=True, methods=['post'])
    def aceitar_entrega(self, request, pk=None):
        pedido = self.get_object()
        user_profile = UserProfile.objects.get(user=request.user)
        
        if user_profile.user_type != 'ENTREGADOR':
            return Response(
                {'error': 'Apenas entregadores podem aceitar entregas'},
                status=status.HTTP_403_FORBIDDEN
            )
            
        if pedido.status != 'A_CONFIRMAR':
            return Response(
                {'error': 'Este pedido não está disponível'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        pedido.entregador = request.user
        pedido.status = 'ACEITO'
        pedido.save()
        
        return Response(self.serializer_class(pedido).data)

    @action(detail=True, methods=['post'])
    def aceitar_travessia(self, request, pk=None):
        pedido = self.get_object()
        user_profile = UserProfile.objects.get(user=request.user)
        
        if user_profile.user_type != 'BARQUEIRO':
            return Response(
                {'error': 'Apenas barqueiros podem aceitar travessias'},
                status=status.HTTP_403_FORBIDDEN
            )
            
        if pedido.status != 'NO_PORTO':
            return Response(
                {'error': 'Este pedido não está disponível para travessia'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        pedido.barqueiro = request.user
        pedido.status = 'EM_TRAVESSIA'
        pedido.save()
        
        return Response(self.serializer_class(pedido).data)
    
    @action(detail=True, methods=['post'])
    def marcar_entregue(self, request, pk=None):
        pedido = self.get_object()
        user_profile = UserProfile.objects.get(user=request.user)
        
        if user_profile.user_type != 'BARQUEIRO':
            return Response(
                {'error': 'Apenas barqueiros podem marcar pedidos como entregues'},
                status=status.HTTP_403_FORBIDDEN
            )
            
        if pedido.status != 'EM_TRAVESSIA' or pedido.barqueiro != request.user:
            return Response(
                {'error': 'Este pedido não pode ser marcado como entregue'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        pedido.status = 'ENTREGUE'
        pedido.save()
        
        return Response(self.serializer_class(pedido).data)
    

class PortoViewSet(viewsets.ModelViewSet):
    queryset = Porto.objects.all()
    serializer_class = PortoSerializer

    @action(detail=True, methods=['get'])
    def pedidos(self, request, pk=None):
        porto = self.get_object()
        pedidos = porto.pedidos_origem.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
    

class PostoViewSet(viewsets.ModelViewSet):
    queryset = Posto.objects.all()
    serializer_class = PostoSerializer

    @action(detail=True, methods=['get'])
    def pedidos(self, request, pk=None):
        posto = self.get_object()
        pedidos = posto.pedidos_destino.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)
    


    
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()  # Changed from User to UserProfile
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def pedidos(self, request, pk=None):
        user_profile = self.get_object()
        # Verifica o tipo de usuário e retorna os pedidos apropriados
        if user_profile.user_type == 'MORADOR':
            pedidos = Pedido.objects.filter(cliente=user_profile.user)
        elif user_profile.user_type == 'ENTREGADOR':
            pedidos = Pedido.objects.filter(entregador=user_profile.user)
        elif user_profile.user_type == 'BARQUEIRO':
            pedidos = Pedido.objects.filter(barqueiro=user_profile.user)
        else:
            pedidos = Pedido.objects.none()
            
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]