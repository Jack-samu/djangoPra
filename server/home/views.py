from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.
def index(req):
    return HttpResponse("Hello, world.\n")

def return_something(req):
    return JsonResponse({'aaa':"哑巴阿巴", 's':"不闻不问"})

def turn_around(req):
    return HttpResponseRedirect("/")

def sayhello(req, name):
    return HttpResponse(f"Hello, {name}.\n")

def echo(req):
    return JsonResponse(req.GET)