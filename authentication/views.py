from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authentication.forms import CreateUserForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('quiz:result-view')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Un compte a été créer pour ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'authentication/register.html', context)


@csrf_protect
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('quiz:result-view')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('quiz:result-view')
            else:
                messages.info(request, "Nom utilisateur OU Mot de passe est incorrect")

        context = {}
        return render(request, 'authentication/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
