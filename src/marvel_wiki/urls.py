from django.urls import path

from marvel_wiki.views.movie import MovieView, UpdateDeleteMovieView

urlpatterns = [
    path("movies", MovieView.as_view()),
    path("movies/<str:MovieId>", UpdateDeleteMovieView.as_view())
]
