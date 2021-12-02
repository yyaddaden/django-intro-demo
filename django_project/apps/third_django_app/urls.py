from django.urls import path
from .views import converter, create, result, history

urlpatterns = [
    path("", converter, name="third_converter"),
    path("converter/", converter, name="third_converter"),
    path("create/", create, name="third_create"),
    path("result/", result, name="third_result"),
    path("history/<str:username>", history, name="third_history"),
]