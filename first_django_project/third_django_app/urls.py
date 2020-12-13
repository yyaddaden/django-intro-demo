from django.urls import path
from .views import converter, create, result, history

urlpatterns = [
    path("converter/", converter, name="converter"),
    path("create/", create, name="create"),
    path("result/", result, name="result"),
    path("history/<str:username>", history, name="history"),
]