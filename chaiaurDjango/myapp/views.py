from django.shortcuts import render

# Create your views here.
def all_myapp(request):
    return render(request, 'myapp/all_myapp.html')