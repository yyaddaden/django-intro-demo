from django.urls import path
from .views import home, converter, result

urlpatterns = [
    path("", home, name="home"),
    path("converter/", converter, name="converter"),
    path("result/", result, name="result"),
]