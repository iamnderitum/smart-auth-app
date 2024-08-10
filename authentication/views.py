from django.shortcuts import render


def authenticate(request):
    return render(request, "authentication/index.html")

