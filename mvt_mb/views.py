from django.http import HttpResponse
from django.shortcuts import render




def inicio(request):
    return HttpResponse('Proyecto de muestra de Familiares')
    