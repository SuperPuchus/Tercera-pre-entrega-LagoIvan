from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('crear_comentario/', views.crear_comentario, name='crear_comentario'),
    path('buscar/', views.buscar, name='buscar'),
]