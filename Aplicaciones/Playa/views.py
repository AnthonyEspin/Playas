from django.shortcuts import render, redirect
from .models import Playa
from django.contrib import messages

def Inicio(request):
    return render(request, "index.html")

# Listar todas las playas
def inicioPlayas(request):
    playas = Playa.objects.all()
    return render(request, "inicio.html", {"playas": playas})

# Formulario para nueva playa
def nuevaPlaya(request):
    return render(request, "nueva.html")

# Guardar nueva playa
def guardarPlaya(request):
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    descripcion = request.POST.get("descripcion", "")

    Playa.objects.create(
        nombre=nombre,
        ubicacion=ubicacion,
        descripcion=descripcion
    )

    messages.success(request, "Playa guardada exitosamente.")
    return redirect('/playas')

# Eliminar playa por ID
def eliminarPlaya(request, id):
    playa = Playa.objects.get(id=id)
    playa.delete()
    messages.success(request, "Playa eliminada exitosamente.")
    return redirect('/playas')

# Mostrar formulario de edición
def editarPlaya(request, id):
    playa = Playa.objects.get(id=id)
    return render(request, "editar.html", {"playa": playa})

# Procesar edición de playa
def procesarEdicionPlaya(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    ubicacion = request.POST["ubicacion"]
    descripcion = request.POST.get("descripcion", "")

    playa = Playa.objects.get(id=id)
    playa.nombre = nombre
    playa.ubicacion = ubicacion
    playa.descripcion = descripcion
    playa.save()

    messages.success(request, "Playa actualizada exitosamente.")
    return redirect('/playas')
