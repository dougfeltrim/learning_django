from django.shortcuts import render

from django.http import HttpResponse

from .models import Cidade

def index(request):

    return HttpResponse("Hello, world. You're at the address index.")

def cities(request, local_id):
    detail_city = Cidade.objects.order_by('nome')[:5]
    output = ' | '.join([q.nome for q in detail_city])
    return HttpResponse(output)


def cep(request, local_id):
    detail_cep = Cidade.objects.order_by('cep')[:5]
    output = ' | '.join([str(c.cep) for c in detail_cep])
    return HttpResponse(output)

'''def display_all(request, local_id):
    output = cities(cidade)
    return HttpResponse(output)
'''
