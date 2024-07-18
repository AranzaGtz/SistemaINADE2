from django.views.generic.list import ListView
from django.utils import timezone
from django.shortcuts import render

from accounts.models import  Notificacion

#   VISTA PARA NOTIFICACIONES DE RECEPCION DE COTIZACIÓN A USUARIO
def notificaciones(request):
    # Aquí obtendrás las notificaciones del usuario
    # Por simplicidad, mostraremos un mensaje de notificación estático
    notificaciones = Notificacion.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'accounts/notificaciones/notificaciones.html', {'notificaciones': notificaciones})
