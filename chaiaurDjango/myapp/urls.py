from django.urls import path
from . import views

# localhost:8000/myapp
# localhost:8000/myapp/order

urlpatterns = [
    path('', views.all_myapp, name='myapp_home'),
]