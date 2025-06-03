from rest_framework import serializers
from .models import Pedido, Porto, Posto, UserProfile
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
    # Campos do User model
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(source='user.email', required=False, allow_blank=True)
    first_name = serializers.CharField(source='user.first_name', required=False, allow_blank=True)
    last_name = serializers.CharField(source='user.last_name', required=False, allow_blank=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'user_type']
        read_only_fields = ['id']

    def create(self, validated_data):
        try:
            print("Received data:", validated_data)  # Debug print
            
            # Extract user data from nested structure
            user_data = validated_data.pop('user', {})
            password = validated_data.pop('password')
            user_type = validated_data.get('user_type')
            
            # Validation
            if not user_data.get('username'):
                raise serializers.ValidationError("Username is required")
            if not password:
                raise serializers.ValidationError("Password is required")
            if not user_type:
                raise serializers.ValidationError("User type is required")
            
            # Create the User instance
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data.get('email', ''),
                first_name=user_data.get('first_name', ''),
                last_name=user_data.get('last_name', ''),
                password=password
            )

            # If user type is ADMIN, make them a superuser
            if user_type == 'ADMIN':
                user.is_staff = True
                user.is_superuser = True
                user.save()
            
            # Create the UserProfile instance
            user_profile = UserProfile.objects.create(
                user=user,
                user_type=user_type
            )
            
            return user_profile
            
        except Exception as e:
            print(f"Error creating user: {str(e)}")
            # If user was created but profile creation failed, delete the user
            if 'user' in locals():
                user.delete()
            raise serializers.ValidationError(str(e))

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        return ret


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
            'descricao', 'valor_proposto', 'valor_final',
            'porto_origem', 'porto_nome',
            'posto_destino', 'posto_nome',
            'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['entregador', 'barqueiro', 'status']






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
