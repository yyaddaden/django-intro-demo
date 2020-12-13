from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return HttpResponse(
        """
            <html>
                <body>
                    <h3>
                        Bienvenue dans la page d'accueil, <a href='http://127.0.0.1:8000/first_app/converter/'>page de conversion</a>
                    </h3>
                </body>
            </html>
        """
    )


def converter(request):
    return HttpResponse(
        """
            <html>
                <body>
                    <h3>
                        Bienvenue dans la page de conversion
                    </h3>

                    <form method='POST' action='http://127.0.0.1:8000/first_app/result/'>
                        <input type='radio' name='user_choice' value='celsius' required />
                        <label>Celsuis</label>

                        <input type='radio' name='user_choice' value='fahrenheit' required />
                        <label>Fahrenheit</label> <br/>

                        <input type='number' step='0.01' name='user_value' required />
                        <input type='submit' value='Calculer' />
                    </form>
                </body>
            </html>
        """
    )


@csrf_exempt
def result(request):
    if request.method == "GET":
        return HttpResponse(
            """
                <html>
                    <body>
                        <h3>
                            Erreur ! <a href='http://127.0.0.1:8000/first_app/converter/'>page de conversion</a>
                        </h3>
                    </body>
                </html>
            """
        )

    elif request.method == "POST":
        user_choice = request.POST.get("user_choice")
        user_value = float(request.POST.get("user_value"))

        if user_choice == "celsius":
            result = "%.2f" % ((user_value * float(9 / 5)) + 32)

            return HttpResponse(
                """
                    <html>
                        <body>
                            <h3>
                                Résultat : {} °C => {} °F | <a href='http://127.0.0.1:8000/first_app/converter/'>page de conversion</a>
                            </h3>
                        </body>
                    </html>
                """.format(
                    user_value, result
                )
            )

        elif user_choice == "fahrenheit":
            result = "%.2f" % ((user_value - 32) * float(5 / 9))

            return HttpResponse(
                """
                    <html>
                        <body>
                            <h3>
                                Résultat : {} °F => {} °C | <a href='http://127.0.0.1:8000/first_app/converter/'>page de conversion</a>
                            </h3>
                        </body>
                    </html>
                """.format(
                    user_value, result
                )
            )