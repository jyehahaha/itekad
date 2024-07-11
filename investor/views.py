from django.shortcuts import render,redirect
from users.models import User,UserProfile
from users.forms import UserForm,UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def LandingView(request):
    context = {}
    return render(request, 'investor/landing.html', context)

@login_required(login_url='login_page')
def HomePageView(request):
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user__id = request.user.id)

    context = {
        'user' : user,
    }
    return render(request, 'investor/home.html', context)

@login_required(login_url='login_page')
def ProfilePageView(request):
    #search user profile using request.user.id
    profile = UserProfile.objects.get(user__id=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            investor = form.save()
            update_session_auth_hash(request, investor)  # Important!
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('home_page')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form' : form
    }
    return render(request, 'investor/profile.html', context)

@login_required(login_url='login_page')
def ChangePasswordPageView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home_page')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form' : form,
    }
    return render(request, 'investor/change_password.html', context)

def GalleryPageView(request):
    context = {}
    return render(request, 'investor/gallery.html', context)

def ReportPageView(request):
    context = {}
    return render(request, 'investor/report.html', context)