from django.shortcuts import render, redirect
from .models import Actividad
from Aplicaciones.Playa.models import Playa
from django.contrib import messages
import os

# Listado de actividades
def inicioActividades(request):
    actividades = Actividad.objects.all()
    return render(request, "inicio_act.html", {"actividades": actividades})

# Formulario nueva actividad
def nuevaActividad(request):
    playas = Playa.objects.all()
    return render(request, "nuevaActividad.html", {"playas": playas})

# Guardar nueva actividad
def guardarActividad(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    playa_id = request.POST["playa"]
    imagen = request.FILES.get("imagen")
    archivo = request.FILES.get("archivo")

    Actividad.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        playa_id=playa_id,
        imagen=imagen,
        archivo=archivo
    )

    messages.success(request, "Actividad guardada exitosamente.")
    return redirect('/actividades')

# Eliminar actividad
def eliminarActividad(request, id):
    actividad = Actividad.objects.get(id=id)

    if actividad.imagen and os.path.isfile(actividad.imagen.path):
        os.remove(actividad.imagen.path)
    if actividad.archivo and os.path.isfile(actividad.archivo.path):
        os.remove(actividad.archivo.path)

    actividad.delete()
    messages.success(request, "Actividad eliminada exitosamente.")
    return redirect('/actividades')

# Mostrar formulario de edición
def editarActividad(request, id):
    actividad = Actividad.objects.get(id=id)
    playas = Playa.objects.all()
    return render(request, "editarActividad.html", {
        "actividad": actividad,
        "playas": playas
    })

# Procesar edición
def procesarEdicionActividad(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    playa_id = request.POST["playa"]
    imagen = request.FILES.get("imagen")
    archivo = request.FILES.get("archivo")

    actividad = Actividad.objects.get(id=id)
    actividad.nombre = nombre
    actividad.descripcion = descripcion
    actividad.playa_id = playa_id

    if imagen:
        if actividad.imagen and os.path.isfile(actividad.imagen.path):
            os.remove(actividad.imagen.path)
        actividad.imagen = imagen

    if archivo:
        if actividad.archivo and os.path.isfile(actividad.archivo.path):
            os.remove(actividad.archivo.path)
        actividad.archivo = archivo

    actividad.save()
    messages.success(request, "Actividad actualizada exitosamente.")
    return redirect('/actividades')
