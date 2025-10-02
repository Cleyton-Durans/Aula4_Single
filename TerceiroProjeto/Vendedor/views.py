from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Vendedor

# Create your views here.

# "request" possui toda a requisição dentro dele.
def listar_clientes(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])
    clientes = Vendedor.objects.all().order_by("nome").values("id","nome","cpf","rg","email","telefone")
    return JsonResponse(list(clientes), safe=False)

