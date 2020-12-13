from django.urls import path, include
from rest_framework import routers

from .views import register, converter, login, logout, HistoryViewSet

router = routers.DefaultRouter()
router.register("history", HistoryViewSet, basename="/")

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("converter/", converter, name="converter"),
    path("", include(router.urls), name="history"),
]