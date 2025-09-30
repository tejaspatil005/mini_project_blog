from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Keep moving Forward......</h1>')

def about(request):
    return HttpResponse('<h1> this is about to end....!!!</h1>')
