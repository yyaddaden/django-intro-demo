from django.shortcuts import render, redirect
from django.utils.timezone import get_current_timezone
from datetime import datetime

from .models import User, History

# Create your views here.


def converter(request):
    users = User.objects.all()
    return render(request, "third_django_app/converter.html", {"users": users})


def create(request):
    if request.method == "GET":
        return redirect("converter")

    elif request.method == "POST":
        username = request.POST.get("username")

        user = User(username=username.lower())
        user.save()

        return render(
            request,
            "third_django_app/create.html",
            {
                "username": username.capitalize(),
            },
        )


def result(request):
    if request.method == "GET":
        return redirect("converter")

    if request.method == "POST":
        username = request.POST.get("usernames").lower()
        user_choice = request.POST.get("user_choice")
        user_value = float(request.POST["user_value"])

        if user_choice == "C":
            result = "%.2f" % ((user_value * float(9 / 5)) + 32)  # fahrenheit

        elif user_choice == "F":
            result = "%.2f" % ((user_value - 32) * float(5 / 9))

        user = User.objects.filter(username=username).first()
        history = History(
            user=user,
            time=datetime.now(tz=get_current_timezone()),
            initial_val=user_value,
            final_val=result,
            initial_met=user_choice,
            final_met="F" if user_choice == "C" else "C",
        )
        history.save()

        return render(
            request,
            "third_django_app/result.html",
            {
                "username": username,
                "initial_met": user_choice,
                "initial_val": "%.2f" % user_value,
                "final_val": result,
            },
        )


def history(request, username):
    user = User.objects.filter(username=username).first()
    histories = user.history_set.all()

    return render(
        request,
        "third_django_app/history.html",
        {
            "username": username,
            "histories": histories,
        },
    )