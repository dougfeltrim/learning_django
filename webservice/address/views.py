from django.shortcuts import render

from django.http import HttpResponse

from .models import Local

def index(request):

    return HttpResponse("Hello, world. You're at the address index.")

def detail(request, local_id):
    detail_local = Local.objects.order_by('-cidade')[:5]
    output = ', '.join([q.cidade for q in detail_local])
    return HttpResponse(output)
