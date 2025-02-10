from django.urls import path
from pokeDexImages.controller.views import PokeDexImageView, PokeDexImageDeleteView, PokeDexImagePostView


urlpatterns = [
    path("<int:number>", PokeDexImageView.as_view()),  # GET 요청
    path("", PokeDexImagePostView.as_view()),  # POST 요청
    path("<int:number>", PokeDexImageDeleteView.as_view()),  # DELETE 요청
]


