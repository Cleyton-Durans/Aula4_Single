from django.contrib import admin
from .models import Vendedor

# Register your models here.

@admin.register(Vendedor)

class VendedorAdmin(admin.ModelAdmin):

    list_display = ('nome', 'email', 'ativo' , 'cpf', 'rg', 'telefone', 'endereco' , 'data_nascimento' , 'sexo', 'ativo', 'criado_em' , 'atualizado_em')

    search_fields = ('nome', 'email')