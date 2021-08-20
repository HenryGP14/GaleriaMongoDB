from django.shortcuts import render
from galeria import models
# Create your views here.


def vw_index(request):
    return render(request, "fanpague.html")

def vw_create(request):
    
    return render(request, "fanpague.html")

