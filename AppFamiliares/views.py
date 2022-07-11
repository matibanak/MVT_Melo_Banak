
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import datetime
from django.template import Context, Template, loader
from AppFamiliares.forms import *


def familiar1(self):

    nom='Julian'
    ape='Bañak'
    fecha_nacim='12/9/1992'
    anios=29
    fecha_hoy=datetime.datetime.today()

    diccionario1={'nombre':nom, 'apellido':ape, 'fecha_nacimiento':fecha_nacim, 'anios':anios, 'fecha_hoy':fecha_hoy}
    MiArchivo= open('C:/Users/Matias/cluster_python/cluster/MVT_MB/mvt_mb/AppFamiliares/Templates/templateApp.html')
    plantilla=Template(MiArchivo.read()) 
    MiArchivo.close()
    contexto=Context(diccionario1) 
    documento=plantilla.render(contexto) 

    return HttpResponse(documento)

def familiar2(self):
    nom='Matias'
    ape='Bañak'
    anios=27
    fecha_hoy=datetime.datetime.today()

    diccionario2={'nombre':nom, 'apellido':ape, 'anios':anios, 'fecha_hoy':fecha_hoy}
    MiArchivo= open('C:/Users/Matias/cluster_python/cluster/MVT_MB/mvt_mb/AppFamiliares/Templates/template2.html')
    plantilla=Template(MiArchivo.read()) 
    MiArchivo.close()
    contexto=Context(diccionario2) 
    documento=plantilla.render(contexto)

    return HttpResponse(documento)
    
def familiar3(self):
    nom='Nicolas'
    ape='Bañak'
    anios=29
    fecha_hoy=datetime.datetime.today()

    diccionario2={'nombre':nom, 'apellido':ape,'anios':anios, 'fecha_hoy':fecha_hoy}
    MiArchivo= open('C:/Users/Matias/cluster_python/cluster/MVT_MB/mvt_mb/AppFamiliares/Templates/template3.html')
    plantilla=Template(MiArchivo.read()) 
    MiArchivo.close()
    contexto=Context(diccionario2) 
    documento=plantilla.render(contexto)

    return HttpResponse(documento)

def fam(self):
    fam=Familiares(nombre='Lorena', apellido='Gonzalez', anios=72)
    fam.save()
    texto=f'Familiar creado: {fam.nombre} {fam.apellido} con {fam.anios}'
    return HttpResponse(texto)

def inicio(request):
    return render (request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/inicio.html")

def familiares(request):
    return render (request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/Familiares.html")

def negocios(request):
    return render (request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/Negocios.html")

def inmobiliarios(request):
    return render (request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/Inmobiliarios.html")


def FamiliaresFormulario(request):

    if (request.method=="POST"):
        form= FamiliarForm(request.POST)
        print(form)
        if form.is_valid():
            info = form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            fecha_nacimiento=["fecha_nacimiento"]
            anios= info["anios"]

            fam= Familiares(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, anios=anios)
            fam.save()
            return render (request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/inicio.html")
    else:
        form=FamiliarForm()
        
    return render(request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/FormFamiliares.html", {"formulario":form})

def NegociosFormulario(request):

    if (request.method=="POST"):
        form= NegociosForm(request.POST)
        print(form)
        if form.is_valid():
            info = form.cleaned_data
            nombre1= info["nombre1"]
            provincia= info["provincia"]
            pais=["pais"]
            telefono= info["telefono"]

            form= Negocios(nombre1=nombre1, provincia=provincia, pais=pais, telefono=telefono)
            form.save()
            return render (request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/inicio.html")
    else:
        form=NegociosForm()
        
    return render(request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/FormNegocios.html", {"formulario":form})

def InmobiliariosFormulario(request):

    if (request.method=="POST"):
        form= InmobiliariosForm(request.POST)
        print(form)
        if form.is_valid():
            info = form.cleaned_data
            direccion= info["direccion"]
            localidad= info["localidad"]
            mt2=info["mt2"]

            form= Inmobiliarios(direccion=direccion, localidad=localidad, mt2=mt2)
            form.save()
            return render (request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/inicio.html")
    else:
        form=InmobiliariosForm()
        
    return render(request, "C:/Users/Matias/cluster_python/cluster/MVT_Grupo_Melo_Bañak/mvt_mb/AppFamiliares/Templates/FormInmobiliarios.html", {"formulario":form})
