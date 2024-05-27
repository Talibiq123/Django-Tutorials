from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello there, You are at Home page")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello there, You are at About page")


def contact(request):
    return HttpResponse("Hello there, You are at Contact page")



