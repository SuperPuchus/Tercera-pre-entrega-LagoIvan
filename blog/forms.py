from django import forms
from .models import Categoria, Publicacion, Comentario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'categoria']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['publicacion', 'autor', 'texto']

class BusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)