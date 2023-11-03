from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views import View

from .forms import RegisterForm, SetPasswordForm
from tasks.models import Task


@login_required(login_url="/login")
def home(request):
    tasks = Task.objects.filter(author_id=request.user.id).order_by('title')
    context = {"tasks": tasks}
    return render(request, 'account/home.html', context)


class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/sign_up_form.html', {'form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User registration is successful.')
            print(request)
            return redirect('/home')

        return render(request, 'registration/sign_up_form.html', {'form': form})


@login_required(login_url="/login")
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed. Login with new password.")
            logout(request)
            return redirect('/login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = SetPasswordForm(user)
    return render(request, 'account/password_change_form.html', {'form': form})
