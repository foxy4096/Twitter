from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from apps.userprofile.forms import UserProfileForm, UserForm


def user_details(request, username):
    """
    View a user's profile.
    """
    tuser = get_object_or_404(User, username=username)
    return render(request, "userprofile/user_profile.html", {"tuser": tuser})


def signup(request):
    """
    Signup a new user.
    """
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            messages.success(request, "You're now a user! You've been signed in, too.")
            return redirect("userprofile:user_details", new_user.username)
    return render(request, "userprofile/signup.html", {"form": form})


@login_required
def edit_profile(request):
    """
    Edit a user's profile.
    """
    if request.method == "POST":
        uform = UserForm(request.POST, instance=request.user)
        pform = UserProfileForm(
            request.POST, request.FILES, instance=request.user.userprofile
        )
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, "Profile updated!")
            return redirect("userprofile:edit_profile")
    uform = UserForm(instance=request.user)
    pform = UserProfileForm(instance=request.user.userprofile)
    return render(
        request, "userprofile/edit_profile.html", {"uform": uform, "pform": pform}
    )
