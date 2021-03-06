from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile
from accounts.forms import UserLoginForm, UserRegistrationForm
from tickets.models import Ticket
from forums.models import Forum


@login_required
def logout(request):
    """
    Log the user out
    """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))


def login(request):
    """
    Return a login page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None,
                                     "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})


def registration(request):
    """
    Render the registration page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                user.profile.save()
                user.profile.points_available = 0
                user.profile.bug_upvotes = 0
                user.profile.feature_upvotes = 0
                user.profile.forum_upvotes = 0
                user.profile.cash_used = 0
                user.profile.save()
                return redirect(reverse('index'))
            else:
                messages.error(request,
                               "Unable to register your account at this time")

    else:
        registration_form = UserRegistrationForm()

    return render(request, "registration.html", {
        "registration_form": registration_form})


@login_required
def user_profile(request):
    """
    The user's profile page
    """
    user = User.objects.get(email=request.user.email)

    bugs = Ticket.objects.filter(type='BUG', author=request.user.username)
    features = Ticket.objects.filter(type='FEATURE',
                                     author=request.user.username)
    forums = Forum.objects.filter(author=request.user.username)
    return render(request, "profile.html", {"profile": user,
                                            "bugs": bugs,
                                            "features": features,
                                            "forums": forums})
