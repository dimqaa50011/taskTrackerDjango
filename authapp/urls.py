from django.contrib import admin
from django.urls import path

from .apps import AuthappConfig

app_name = AuthappConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
]
