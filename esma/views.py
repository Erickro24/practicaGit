from django.http import HttpResponse
from django.shortcuts import render

def inicio (request):

    return render(request, "index.html")

def blog1 (request):

    return render(request, "blog1.html")
def blog2 (request):

    return render(request, "blog2.html")