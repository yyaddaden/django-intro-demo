from django.shortcuts import render, redirect

# Create your views here.


def converter(request):
    return render(request, "second_django_app/converter.html")


def result(request):
    if request.method == "GET":
        return redirect("converter")

    elif request.method == "POST":
        user_choice = request.POST.get("user_choice")
        user_value = float(request.POST["user_value"])

        if user_choice == "celsius":
            result = "%.2f" % ((user_value * float(9 / 5)) + 32)  # fahrenheit

        elif user_choice == "fahrenheit":
            result = "%.2f" % ((user_value - 32) * float(5 / 9))

        return render(
            request,
            "second_django_app/result.html",
            {
                "initial_metric": user_choice,
                "initial_value": "%.2f" % user_value,
                "final_value": result,
            },
        )
