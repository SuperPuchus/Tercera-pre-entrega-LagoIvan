from django.shortcuts import render, get_object_or_404
from .models import Categoria, Publicacion, Comentario
from .forms import CategoriaForm, PublicacionForm, ComentarioForm, BusquedaForm

def index(request):
    return render(request, 'blog/index.html')

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'blog/form.html', {'form': form})

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PublicacionForm()
    return render(request, 'blog/form.html', {'form': form})

def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComentarioForm()
    return render(request, 'blog/form.html', {'form': form})

def buscar(request):
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Publicacion.objects.filter(titulo__icontains=query)
            return render(request, 'blog/resultados.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'blog/buscar.html', {'form': form})
