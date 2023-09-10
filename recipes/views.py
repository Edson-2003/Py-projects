from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
	return HttpResponse('home')

def contato(request):
	return HttpResponse('contato')
