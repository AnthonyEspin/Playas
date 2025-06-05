from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio),
    path('playas', views.inicioPlayas),
    path('nuevaPlaya', views.nuevaPlaya),
    path('guardarPlaya', views.guardarPlaya),
    path('eliminarPlaya/<int:id>', views.eliminarPlaya),
    path('editarPlaya/<int:id>', views.editarPlaya),
    path('procesarEdicionPlaya', views.procesarEdicionPlaya),
]