from django.urls import path

from . import views


urlpatterns = [
    path('human/<int:pk>', views.HumanDetailView.as_view()),
    path('human/', views.HumanListView.as_view())
]
