from django.urls import path
from .views import ola_mundo

urlpatterns = [
    path('', ola_mundo),
]
