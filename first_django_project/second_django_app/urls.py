from django.urls import path
from .views import converter, result

urlpatterns = [
    path("converter/", converter, name="converter"),
    path("result/", result, name="result"),
]