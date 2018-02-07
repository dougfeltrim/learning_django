from django.shortcuts import render
from django.http import HttpResponse

from .models import Sell


def index(request):
    return HttpResponse("Hello, world. You're at the shop index.")

def detail(request, sell_id):
    return HttpResponse("You're looking   %s." % sell_id )

def results(request, sell_id):
    response = "You're looking sell name  %s." % sell_id
    return HttpResponse(response % sell_id)

def price(request, sell_id):
    return HttpResponse("You're looking sell price    %s." % sell_id)

def amount(request, sell_id):
        return HttpResponse("You're looking sell amount    %s." % sell_id)
