from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPES = [
        ('MORADOR', 'Morador'),
        ('ENTREGADOR', 'Entregador'),
        ('BARQUEIRO', 'Barqueiro'),
        ('ADMIN', 'Administrador')
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"

class Porto(models.Model):
    nome = models.CharField(max_length=100)
    doca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Posto(models.Model):
    nome = models.CharField(max_length=100)
    armario = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(User, related_name='pedidos_cliente', on_delete=models.CASCADE)
    entregador = models.ForeignKey(User, related_name='pedidos_entregador', null=True, blank=True, on_delete=models.SET_NULL)
    barqueiro = models.ForeignKey(User, related_name='pedidos_barqueiro', null=True, blank=True, on_delete=models.SET_NULL)
    descricao = models.TextField()
    valor_proposto = models.DecimalField(max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    porto_origem = models.ForeignKey(Porto, related_name='pedidos_origem', on_delete=models.PROTECT)
    posto_destino = models.ForeignKey(Posto, related_name='pedidos_destino', on_delete=models.PROTECT)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('A_CONFIRMAR', 'Aguardando Confirmação'),
            ('ACEITO', 'Aceito pelo Entregador'),
            ('EM_TRANSITO', 'Em Trânsito para Porto'),
            ('NO_PORTO', 'Entregue ao Porto'),
            ('EM_TRAVESSIA', 'Em Travessia'),
            ('NO_POSTO', 'No Posto de Destino'),
            ('ENTREGUE', 'Entregue ao Cliente'),
            ('CONCLUIDO', 'Concluído')
        ],
        default='A_CONFIRMAR'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.username}"