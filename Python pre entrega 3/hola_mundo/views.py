from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse('hola mundo')
def saludar_a(request, alguien):
    return HttpResponse(f"Hola como estas {alguien}")
def sumar(request, a, b):
    return HttpResponse(f"el resultado de a+b es = {a+b}")
def mostrar_mi_template(request, Nombre, Apellido):
    context = {
        "Nombre": Nombre,
        "Apellido": Apellido,
        "notas": [1,3,8,9,9,7,8,9,9]
    }
    return render(request, "hola_mundo/index.html")

def mostrar_mis_tareas(request, criterio):
    if criterio:
        tareas = Tarea.objects.all()
    elif criterio == "todo":
        tareas = Tarea.objects.filter(nombre=criterio).all()
    return render (request, "hola_mundo/tareas.html", {"tareas" : tareas})

def mostrar_personas(request):
    personas = personas.objects.all()
    return render (request, "hola_mundo/personas.html", {"personas": personas}, {"total_personas": total_personas})

def mascota(request):
    mascota = mascota.objects.all()
    return render (request, "hola_munddo/mascota.html", {"mascota": mascota}, {"total_mascota": total_mascota})