from django.urls import path
from pokeDexImages.controller.views import PokeDexImageView

urlpatterns = [
    path('<int:number>', PokeDexImageView.as_view()),
]
