from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path("add_todo/", views.add_todo, name="add_todo"),

    path("update-todo/<str:pk>/", views.update_todo, name="update-todo"),
]