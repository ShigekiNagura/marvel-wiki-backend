from django.urls import path

from marvel_wiki.views import SampleView

urlpatterns = [
    path("sample", SampleView.as_view()),
]
