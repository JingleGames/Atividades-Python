from django.shortcuts import render

from django.http import HttpResponse

def ola_mundo(request):
    return HttpResponse("Olá, mundo! Bem-vindo ao Django.")

