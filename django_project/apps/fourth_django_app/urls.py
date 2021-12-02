from django.urls import path, include
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import register, converter, login, logout, HistoryViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Conversion de Température",
        default_version="v1.0",
        description="Application de Conversion de Température",
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register("history", HistoryViewSet, basename="/")

urlpatterns = [
    path("", register, name="fourth_register"),
    path("register/", register, name="fourth_register"),
    path("login/", login, name="fourth_login"),
    path("logout/", logout, name="fourth_logout"),
    path("converter/", converter, name="fourth_converter"),
    path("", include(router.urls), name="fourth_history"),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
