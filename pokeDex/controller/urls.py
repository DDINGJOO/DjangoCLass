
from django.urls import path
from .views import PokeDexInsertView, PokeDexByIdView, PokeDexBySortByNameView, PokeDexListView, PokeDexByNameView

urlpatterns = [
    path('insert/until/<int:number>', PokeDexInsertView.as_view()),
    path('name/<str:name>/', PokeDexByNameView.as_view()),
    path('number/<int:number>/', PokeDexByIdView.as_view()),
    path('name/<str:name>/', PokeDexBySortByNameView.as_view()),
    path('list/<str:order>/', PokeDexListView.as_view()),
]

