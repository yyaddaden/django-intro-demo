from django.urls import path
from .views import home, converter, result

urlpatterns = [
    path("", converter, name="first_converter"),
    path("converter/", converter, name="first_converter"),
    path("result/", result, name="first_result"),
]