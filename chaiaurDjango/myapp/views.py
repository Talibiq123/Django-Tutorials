from .models import ChaiVarity
from django.shortcuts import render, get_object_or_404

# Create your views here.
def all_myapp(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'myapp/all_myapp.html', {'chais': chais})


def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVarity, pk=chai_id)
  return render(request, 'myapp/chai_detail.html', {'chai': chai})