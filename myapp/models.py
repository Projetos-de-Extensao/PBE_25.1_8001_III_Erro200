from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    cliente = models.ForeignKey(User,on_delete=models.CASCADE)  
    itens = models.ManyToManyField(Item)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('Solicitado', 'Solicitado'),
            ('Aceito', 'Aceito'),
            ('Em trânsito', 'Em trânsito'),
            ('Entregue', 'Entregue'),
            ('Concluído', 'Concluído')
        ]
    )

    def __str__(self):
        return f"{self.cliente.username if self.cliente else 'No cliente'}"