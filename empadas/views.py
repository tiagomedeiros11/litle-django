from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse('Empadas')

def contato(request):
    return HttpResponse('Contato')
