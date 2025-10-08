from django.shortcuts import render
from .models import Funcion

# Create your views here.
def index(request):
    funciones = Funcion.objects.all()
    return render(request, 'index.html', {'funciones':funciones})