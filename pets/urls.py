from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pets, name='listar_pets'),
    path('<int:pet_id>/', views.detalhar_pet, name='detalhar_pet'),
]