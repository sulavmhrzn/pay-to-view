from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .decorators import anonymous_user_required
from .forms import UserCreationForm


@anonymous_user_required
def signup_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("account:login")
    return render(request, "account/signup.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html")
