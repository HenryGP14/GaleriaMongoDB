from django.shortcuts import render

# Create your views here.


def vw_login(response):
    return render(response, "session.html")
