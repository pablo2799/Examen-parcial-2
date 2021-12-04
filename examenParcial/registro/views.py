from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import render
from .models import comentarios
from django.views import generic
# Create your views here.
def regObservaciones(request):
    num_comentarios=comentarios.objects.all().count()
    return render(request,'formulario.html', context={"num_comentarios":num_comentarios})

def resultado(request):
    mensaje=request.GET["observaciones"]
    return HttpResponse(mensaje)