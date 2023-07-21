from django.urls import path
from . import views

# prin punct importez views din acelasi folder cu urls.py

urlpatterns = [
    path('', views.PaginaPrincipala.as_view(), name='home'), # acel string gol reprezinta adresa url unde e afisata PaginaPrincipala
    path('item/<int:pk>/', views.MasinaDetalii.as_view(), name = 'adresa_item'),
    path('about', views.About.as_view(), name = 'about')
]



# .as_view e o metoda care reda aceasta clasa ca o vizualizare reala cu vizualizari bazate pe functii