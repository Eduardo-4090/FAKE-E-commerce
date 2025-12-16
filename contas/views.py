from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        nome = request.POST.get('username').lower()
        senha = request.POST.get('password').lower()

        try:
            if not nome or not senha:
                messages.error(request ,'Todos os campos são obrigatórios.')
                return redirect('login')
            
            user = authenticate(request , username=nome , password=senha )
            if user is not None:
                login(request, user)
                return redirect('home')
        except:
            messages.error(request ,' Algo deu errado , tente novamente')
            return redirect('login')

    else:
        return render(request , 'login.html')

def sign_up(request):
    if request.method =="POST":
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        try:
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuario já em uso')
                return redirect('cadastro')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email já em uso')
                return redirect('cadastro')
            
            elif not nome or not email or not senha:
                messages.error(request, 'Todos os campos são obrigatórios.')
                return redirect('cadastro')
            else:
                usuario =User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha
                )
                messages.success(request, 'Conta criada com success')
                return redirect('login')
        except:
            messages.error(request , 'Algo deu errado tente novamente')
            return redirect('cadastro')

    else:
        return render(request , 'sign_up.html')
