from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from tarefas.models import Usuario
from requests_oauthlib import OAuth2Session
from django.conf import settings

def cadastro(request):
    if request.user.is_authenticated:
        messages.info(request, "Você já está cadastrado e logado!")
        return redirect('home')

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '').strip()
        confirmacao_senha = request.POST.get('confirmacao_senha', '').strip()

        if not nome or not email or not senha or not confirmacao_senha:
            messages.warning(request, "Preencha todos os campos.")
            return render(request, 'auth/cadastro.html', {'nome': nome, 'email': email})

        if senha != confirmacao_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'auth/cadastro.html', {'nome': nome, 'email': email})

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Email já cadastrado.")
            return render(request, 'auth/cadastro.html', {'nome': nome, 'email': email})

        usuario = Usuario(email=email, nome=nome)
        usuario.set_password(senha)
        usuario.save()

        messages.success(request, "Cadastro realizado com sucesso! Você já pode fazer login.")
        return redirect('login')

    return render(request, 'auth/cadastro.html')

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "Você já está logado!")
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '').strip()

        if not email or not senha:
            messages.warning(request, "Preencha todos os campos.")
            return render(request, 'auth/login.html', {'email': email})

        usuario = authenticate(request, email=email, password=senha)

        if usuario:
            login(request, usuario)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Email ou senha incorretos.")
            return render(request, 'auth/login.html', {'email': email})

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def google_login(request):
    google = OAuth2Session(
        settings.GOOGLE_OAUTH2_CLIENT_ID,
        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URI,
        scope=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
    )

    authorization_url, state = google.authorization_url(
        'https://accounts.google.com/o/oauth2/auth',
        access_type="offline",
        prompt="select_account"
    )

    request.session['oauth_state'] = state

    return redirect(authorization_url)
    
def google_callback(request):
    if 'oauth_state' not in request.session:
        return redirect('login') 
    
    google = OAuth2Session(
        settings.GOOGLE_OAUTH2_CLIENT_ID,
        redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT_URI,
        state=request.session['oauth_state']
    )

    token = google.fetch_token(
        'https://accounts.google.com/o/oauth2/token',
        client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        authorization_response=request.build_absolute_uri()
    )

    response = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
    user_info = response.json()

    email = user_info.get('email')
    nome = user_info.get('name')
    google_id = user_info.get('id')

    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        usuario = Usuario.objects.create(
            email=email,
            nome=nome,
            google_id=google_id, 
        )
    else:
        usuario.google_id = google_id
        usuario.save()

    login(request, usuario, backend='tarefas.backends.EmailBackend')

    return redirect('login')