from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import item
# Create your views here.
def index(request):
    product = item.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'item': product
    }
    return HttpResponse(template.render(context, request))

def search(request):
    name = request.GET['search']
    result = item.objects.filter(name__icontains=name)
    template = loader.get_template('search_result.html')
    context = {
        'item' : result
    }
    return HttpResponse(template.render(context, request))

def back(request):
    return HttpResponseRedirect(reverse('index'))