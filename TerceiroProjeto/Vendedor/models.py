from django.db import models

# Create your models here.
class Vendedor(models.Model):

    sexo_choises = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    ativo = models.BooleanField(default=True)
    cpf = models.CharField()
    rg = models.CharField()
    telefone = models.CharField()
    endereco = models.CharField()
    data_nascimento =  models.DateField()
    sexo = models.CharField(max_length=1, choices=sexo_choises, blank=False, null=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now_add=True)