from django.shortcuts import render

from django.http import HttpResponse

from .models import Local

def index(request):

    return HttpResponse("Hello, world. You're at the address index.")

def cities(request, local_id):
    detail_city = Local.objects.order_by('cidade')[:5]
    output = ' | '.join([q.cidade for q in detail_city])
    return HttpResponse(output)


def cep(request, local_id):
    detail_cep = Local.objects.order_by('cep')[:5]
    output = ' | '.join([str(c.cep) for c in detail_cep])
    return HttpResponse(output)
