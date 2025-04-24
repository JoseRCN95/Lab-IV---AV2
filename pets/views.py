from django.shortcuts import render, get_object_or_404
from .models import Pet
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SolicitacaoAdocao
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def cadastro_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar')

        if senha != confirmar:
            messages.error(request, 'Senhas não coincidem.')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('login')

    return render(request, 'cadastro.html')

def listar_pets(request):
    pets = Pet.objects.all()
    return render(request, 'pets/listar.html', {'pets': pets})

def detalhar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pets/detalhar.html', {'pet': pet})

@login_required
def adotar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == 'POST':
        nome_pessoa = request.POST.get('nome')
        idade_pessoa = request.POST.get('idade')
        endereco = request.POST.get('endereco')

        SolicitacaoAdocao.objects.create(
            pet=pet,
            nome_pessoa=nome_pessoa,
            idade_pessoa=idade_pessoa,
            endereco=endereco
        )

        messages.success(request, 'Solicitação de adoção enviada com sucesso!')
        return redirect('listar_pets')

    return render(request, 'adotar.html', {'pet': pet})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listar_pets')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')