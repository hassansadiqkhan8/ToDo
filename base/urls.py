from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.register_user, name="register"),

    path("", views.home, name="home"),

    path("add_todo/", views.add_todo, name="add_todo"),

    path("update-todo/<str:pk>/", views.update_todo, name="update-todo"),

    path("delete-todo/<str:pk>/", views.delete_todo, name="delete-todo"),
    
]