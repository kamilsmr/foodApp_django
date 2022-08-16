from email.header import Header
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.

def index(request):
    item_list=Item.objects.all()
    
    context = {
        'item_list':item_list,

    }
    return HttpResponse(request,'food/index.html',context)


def item(request):
    return HttpResponse('<h1>This is an item view</h1> ')