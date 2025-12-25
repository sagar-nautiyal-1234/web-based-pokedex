from django.urls import path
from . import views

urlpatterns = [
    # Home page → Pokémon list (pagination)
    path('', views.pokemon_list, name='pokemon_list'),

    # Pokémon detail page
    path('pokemon/<str:name_or_id>/', views.pokemon_detail, name='pokemon_detail'),

    # Region Pokédex (Kanto, Johto, Hoenn, etc.)
    path('region/<str:region_name>/', views.region_pokedex, name='region_pokedex'),
]
