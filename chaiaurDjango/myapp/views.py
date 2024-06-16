# from .models import ChaiVarity
from .models import ChaiVarity, Store
from .forms import ChaiVarityForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def all_myapp(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'myapp/all_myapp.html', {'chais': chais})


def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVarity, pk=chai_id)
  return render(request, 'myapp/chai_detail.html', {'chai': chai})


def chai_store_view(request):
  stores = None
  if request.method == 'POST':
    form = ChaiVarityForm(request.POST)
    if form.is_valid():
      chai_variety = form.cleaned_data['chai_variety']
      stores = Store.objects.filter(chai_varieties=chai_variety)
  else:
    form = ChaiVarityForm()

  return render(request, 'myapp/chai_stores.html', {'form': form, 'stores': stores})

