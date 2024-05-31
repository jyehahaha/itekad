from django.shortcuts import render, redirect
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("mykad_no", "mobile_no", "country")

# Create your views here.
@login_required
@transaction.atomic
def UpdateprofileView(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect("user:profile")
    else:
        user_form = UserForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "profile.html", {"u_form":user_form, "p_form": user_profile_form})

def LoginView(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			messages.success(request, ("You Have Been Logged In!"))
			return redirect('user_management_page')
		else:
			messages.success(request, ("There was an error, please try again..."))
			return redirect('login_page')

	else:
		return render(request, 'users/login.html', {})

def LogoutView(request):
	logout(request)
	messages.success(request, ("You have been logged out...Thanks for stopping by..."))
	return redirect('home')

def RegisterView(request):
  form = UserForm()
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
			# log in user
      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
      return redirect('user_management_page')
    else:
      messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
      return redirect('register')
  else:
    return render(request, 'users/register.html', {'form':form})  

def ForgotPasswordView(request):
  context = {}
  return render(request, 'users/forgot_password.html', context)

def ResetPasswordView(request):
  context = {}
  return render(request, 'users/reset_password.html', context)

def SuccessPasswordView(request):
  context = {}
  return render(request, 'users/success_password.html', context)

def EnableDisableView(request):
  context = {}
  return render(request, 'users/user_management.html', context)

def SendPassword(request):
  context = {}
  return render(request, 'users/send_password.html', context)

def UserManagementView(request):
  context = {}
  return render(request, 'users/user_management.html', context)

def CreateUserManagementView(request):
  context = {
    'view': 'create'
  }
  return render(request, 'users/crud_user_management.html', context)

def UpdateUserManagementView(request,id):
  context = {
     'view': 'update'
  }
  return render(request, 'users/crud_user_management.html', context)

def DeleteUserManagementView(request,id):
  context = {
     'view': 'delete'
  }
  return render(request, 'users/crud_user_management.html', context)

def DetailsUserManagementView(request,id):
  context = {
      'view': 'details'
  }
  return render(request, 'users/crud_user_management.html', context)
