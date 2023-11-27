from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    sobrenome = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=50,
        null=False,
        blank=False
    )

    objetos = models.Manager()
    def __str__(self):
        return f'ID:{self.id} - {self.nome}'

class Produto(models.Model):
    nome_produto = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    preco = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        blank=False
    )
    objetos = models.Manager()
    def __str__(self):
        return f'ID:{self.id} - {self.nome_produto}'

class Venda(models.Model):
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        'Produto',
        on_delete=models.CASCADE
    )

    data_hora = models.DateTimeField(
        auto_now_add=True
    )
    objetos = models.Manager()


class Fila(models.Model):
    venda = models.ForeignKey(
        'Venda',
        on_delete=models.CASCADE
    )
    objetos = models.Manager()

