from django.urls import path
from . import views

urlpatterns = [
    # Rota para página inicial 
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]