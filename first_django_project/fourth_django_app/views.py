from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.utils.timezone import get_current_timezone
from datetime import datetime

from .models import History
from .serializers import HistorySerializer

# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, "fourth_django_app/register.html", {"status": False})
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User(username=username, password=make_password(password))
        user.save()

        return render(request, "fourth_django_app/register.html", {"status": True})


@api_view(["POST"])
def login(request):
    username = request.data["username"]
    password = request.data["password"]

    user = User.objects.filter(username=username)

    if user.exists():
        auth_success = check_password(password, user.first().password)

        if auth_success:
            token = Token.objects.filter(user=user.first())

            if token.exists():
                return Response(
                    {"token": "Token {}".format(token.first().key)},
                    status=status.HTTP_200_OK,
                )
            else:
                token = Token.objects.create(user=user.first())
                return Response(
                    {"token": "Token {}".format(token.key)}, status=status.HTTP_200_OK
                )

            return Response(
                {"message": "L'utilisateur existe !"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Mot de passe incorrect !"},
                status=status.HTTP_404_NOT_FOUND,
            )
    else:
        return Response(
            {"message": "L'utilisateur n'existe pas !"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout(request):
    token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]

    invalidated_token = Token.objects.filter(key=token_key).first()
    invalidated_token.delete()

    return Response(
        {"message": "Deconnexion effectuée avec succès !"}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def converter(request):
    initial_met = request.data["initial_met"]
    initial_val = float(request.data["initial_val"])
    final_met = request.data["final_met"]

    if initial_met == "C":
        result = "%.2f" % ((initial_val * float(9 / 5)) + 32)  # fahrenheit

    elif initial_met == "F":
        result = "%.2f" % ((initial_val - 32) * float(5 / 9))

    token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
    user = Token.objects.filter(key=token_key).first().user

    history = History(
        user=user,
        time=datetime.now(tz=get_current_timezone()),
        initial_val=initial_val,
        final_val=result,
        initial_met=initial_met,
        final_met=final_met,
    )
    history.save()

    return Response(
        {
            "message": "En convertissant {} °{}, on obtient {} °{}.".format(
                "%.2f" % (initial_val), initial_met, result, final_met
            ),
        },
        status=status.HTTP_200_OK,
    )


class HistoryViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        token_key = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
        user = Token.objects.filter(key=token_key).first().user

        histories = user.history_set.all()
        print(histories)
        histories_serializer = HistorySerializer(histories, many=True)

        return Response(
            {
                "username": user.username,
                "data": histories_serializer.data,
            },
            status=status.HTTP_200_OK,
        )