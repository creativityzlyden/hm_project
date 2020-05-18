from django.urls import path

from . import views


urlpatterns = [
    path("match/<int:pk>", views.MatchDetailView.as_view()),
    path("match/", views.MatchListView.as_view())
]
