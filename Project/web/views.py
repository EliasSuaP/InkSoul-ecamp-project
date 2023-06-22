from django.shortcuts import render
from web.models import Animale, Reserva, Maorie, Mitologico, Tatuadores, Producto
from web.forms import FormReserva
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')


# Formulario
def reserva(request):
    return render(request, 'reserva.html')


def reserva(request):
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            reserva = Reserva.objects.create(**form.cleaned_data)
        #reserva.save()
        return HttpResponseRedirect('Gracias')
    else:
        form = FormReserva()
    return render(request, 'reserva.html', {'form':form})


# template de agradecimiento personalizado al enviar el formulario
def gracias(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    return render(request, 'gracias.html', {'nombre': nombre, 'apellido': apellido})


# template sección de tatuadores
def tatuadores(request):
    context = Tatuadores.objects.all()
    return render(request, 'tatuadores.html', {'context': context})


# Venta kit
def kit(request):
    context = Producto.objects.all()
    return render(request, 'kit.html', {'context':context})


# Galerias de imágenes
def animales(request):
    context = Animale.objects.all()
    return render(request, 'animales.html', {'context': context})


def maories(request):
    context = Maorie.objects.all()
    return render(request, 'maories.html', {'context': context})


def mitologicos(request):
    context = Mitologico.objects.all()
    return render(request, 'mitologicos.html', {'context' : context})
