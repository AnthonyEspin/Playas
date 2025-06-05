from django.urls import path
from . import views

urlpatterns = [
    path('actividades', views.inicioActividades),
    path('nuevaActividad', views.nuevaActividad),
    path('guardarActividad', views.guardarActividad),
    path('eliminarActividad/<int:id>', views.eliminarActividad),
    path('editarActividad/<int:id>', views.editarActividad),
    path('procesarEdicionActividad', views.procesarEdicionActividad),
]