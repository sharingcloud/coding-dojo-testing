"""Views."""

from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET

from .forms import LoginForm

from .models import Profile


def login(request):
    errors = {}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = form.cleaned_data.get("user")
            if user is None:
                user = User()
                user.username = username
                user.set_password(password)
                user.save()

                profile = Profile()
                profile.user = user
                profile.save()

            auth_login(request, user)
            return redirect("/home")

        else:
            errors = form.errors

    context = {
        "errors": errors
    }

    return render(request, 'testme/login.html', context)


@require_GET
def logout(request):
    auth_logout(request)
    return redirect("/login")


@login_required
@require_GET
def home(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request, "testme/home.html", {
        "profile": profile
    })
