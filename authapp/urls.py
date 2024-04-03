from django.contrib import admin
from django.urls import path

from .apps import AuthappConfig
from . import views as auth_views

app_name = AuthappConfig.name

urlpatterns = [
    path('login/', auth_views.CustomLoginView.as_view(), name="login"),
    path('logout/', auth_views.CustomLogoutView.as_view(), name="logout"),
]
