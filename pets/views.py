from django.shortcuts import render, get_object_or_404
from .models import Pet

def listar_pets(request):
    pets = Pet.objects.all()
    return render(request, 'pets/listar.html', {'pets': pets})

def detalhar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pets/detalhar.html', {'pet': pet})