from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    return HttpResponse('teste')

def mysobre(request):
    return HttpResponse('teste')

def mycontato(request):
    return HttpResponse('teste')