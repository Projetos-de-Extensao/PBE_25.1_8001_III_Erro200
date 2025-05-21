from rest_framework import serializers
from .models import Pedido, Item, Porto, Posto, UserProfile
from django.contrib.auth.models import User


class PortoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Porto
        fields = ['id', 'nome', 'doca']
        read_only_fields = ['id']

class PostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posto
        fields = ['id', 'nome', 'armario']
        read_only_fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
        read_only_fields = ['id']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'user_type']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        
        # Create User instance
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data.get('email', ''),
            password=password,
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', '')
        )
        
        # Create UserProfile instance
        user_profile = UserProfile.objects.create(
            user=user,
            **validated_data
        )
        
        return user_profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        
        if user_data:
            # Update User instance
            user = instance.user
            password = user_data.pop('password', None)
            
            for attr, value in user_data.items():
                setattr(user, attr, value)
                
            if password:
                user.set_password(password)
                
            user.save()
            
        # Update UserProfile instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        instance.save()
        return instance


class PedidoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.username', read_only=True)
    entregador_nome = serializers.CharField(source='entregador.username', read_only=True)
    barqueiro_nome = serializers.CharField(source='barqueiro.username', read_only=True)
    porto_nome = serializers.CharField(source='porto_origem.nome', read_only=True)
    posto_nome = serializers.CharField(source='posto_destino.nome', read_only=True)

    class Meta:
        model = Pedido
        fields = [
            'id', 'cliente', 'cliente_nome', 
            'entregador', 'entregador_nome',
            'barqueiro', 'barqueiro_nome',
            'itens', 'valor_proposto', 'valor_final',
            'porto_origem', 'porto_nome',
            'posto_destino', 'posto_nome',
            'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['entregador', 'barqueiro', 'status']


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

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
            'last_login'
        ]
        read_only_fields = ['id', 'date_joined', 'last_login']
        extra_kwargs = {
            'is_active': {'default': True},
            'is_staff': {'default': False},
            'is_superuser': {'default': False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password) 
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)
