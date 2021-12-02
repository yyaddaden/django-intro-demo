from django.urls import path
from .views import converter, result

urlpatterns = [
    path("", converter, name="second_converter"),
    path("converter/", converter, name="second_converter"),
    path("result/", result, name="second_result"),
]