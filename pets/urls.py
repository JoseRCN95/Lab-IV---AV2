from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('', views.listar_pets, name='listar_pets'),
    path('<int:pet_id>/', views.detalhar_pet, name='detalhar_pet'),
    path('pet/<int:pet_id>/adotar/', views.adotar_pet, name='adotar_pet'),
]