from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.core.paginator import (
  Paginator,
  EmptyPage,
  PageNotAnInteger,
)
from .filters import UserFilter
from .models import (
  User,
  UserProfile,
)
from .forms import (
  UserLoginForm,
  UserForm,
  UserProfileForm,
  UserUpdateForm,
)

# Create your views here.
def LoginView(request):
  # login form
  form = UserLoginForm()

  # form post
  if request.method == "POST":
    # form submit
    form = UserLoginForm(request=request, data=request.POST)

    # form valid
    if form.is_valid():
      # clean data
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']

      # authenticate
      user = authenticate(request, username=username, password=password)

      # user authenticate or not
      if user is not None:
        # login user
        login(request, user)

        #  fetch user profile
        profile = UserProfile.objects.get(user=user)

        # check user role
        if profile.role == "INVESTOR":
          # message success
          messages.success(request, f"Welcome, {username}! You are now logged in.")
          # redirect to investor home page
          return redirect('home_page')
        else:
          # message success
          messages.success(request, f"Welcome, {username}! You are now logged in.")
          # redirect to sfd admin dashboard
          return redirect('dashboard_page')
      # user authenticate error
      else:
        messages.error(request, "Your account could not be authenticated. Please verify your login details.")

  context = {
    'form': form,
  }
  return render(request, 'users/login.html', context)

def LogoutView(request):
	logout(request)
	messages.success(request, "You have been logged out. Come back soon!")
	return redirect('login_page')

def RegisterView(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    profile_form = UserProfileForm(request.POST)

    if form.is_valid() and profile_form.is_valid() and form.cleaned_data['terms_agreement']:
      user = form.save(commit=False)
      user.save()
      
      try:
        profile = UserProfile.objects.get(user=user)
      except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

      # Update the profile fields from the form
      profile_form = UserProfileForm(request.POST, instance=profile)
      profile_form.save()
      
      # Assign role to 'INVESTOR'
      profile.role = 'INVESTOR'
      profile.save()

      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
			
      # log in user
      user = authenticate(username=username, password=password)
      login(request, user)


      messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
      return redirect('home_page')

    else:
      messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
      return redirect('register_page')
  else:
    form = UserForm()
    profile_form = UserProfileForm()
  
  return render(request, 'users/register.html', {'form':form, 'profile_form':profile_form})

def ResetPasswordView(request):
  context = {}
  return render(request, "users/reset_password.html", context)

def SuccessPasswordView(request):
  context = {}
  return render(request, 'users/success_password.html', context)

def EnableDisableView(request):
  context = {}
  return render(request, 'users/user_management.html', context)

def SendPassword(request, id):
	# Fetch User
  user = User.objects.get(id=id)
  
	# send email
  form = PasswordResetForm({'email': user.email})
  assert form.is_valid()
		# send email
  form.save(request=request,from_email="mr.alif.93@gmail.com")
  
  context = {}
  return render(request, 'users/send_password.html', context)

def UserManagementView(request):
    if request.user.is_authenticated:
        # Look Up Records
        user_profile_record = UserProfile.objects.filter(user__is_superuser=False)

        # filter
        f = UserFilter(request.GET, queryset=user_profile_record)

        # variable for paginator
        page_num = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)

        # pass the list for pagination
        paginator = Paginator(f.qs, limit)

        # paginator
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)

        context = {
          'filter': f,
          'page_obj': page_obj,
          'dashboard_view': True,
          'user_profile_record':user_profile_record
        }

        return render(request, 'users/user_management.html', context)
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('login_page')
    
def CreateUserManagementView(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST)
    profile_form = UserProfileForm(request.POST)
    user_form.terms_agreement = True

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save(commit=False)
      user.save()
        
      try:
        profile = UserProfile.objects.get(user=user)
      except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

      # Update the profile fields from the form
      profile_form = UserProfileForm(request.POST, instance=profile)
      profile_form.save()

      return redirect('user_management_page')  # Redirect to the user management page after registration
  else:
    user_form = UserForm()
    profile_form = UserProfileForm()

  context = {
    'view': 'create',
    'form1': user_form,
    'form2': profile_form,
  }
  return render(request, 'users/crud_user_management.html', context)

def UpdateUserManagementView(request,id=None):
  if request.method == "POST":
    # Get Current User
    current_user = User.objects.get(id=id)
    # Get Current User's Profile
    profile_user = UserProfile.objects.get(user__id=id)

    form = UserUpdateForm(request.POST or None, instance=current_user)
    profile_form = UserProfileForm(request.POST or None, instance=profile_user)

    if form.is_valid() and profile_form.is_valid():
      form.save()
      profile_form.save()
      messages.success(request, "Your Info Has Been Updated!!")
      return redirect('user_management_page')
    else:
       print(form.errors)
       print(profile_form.errors)
  else:
    current_user = User.objects.get(id=id or request.user.id)
    profile_user = UserProfile.objects.get(user__id=id or request.user.id)

  form = UserUpdateForm(instance=current_user)
  profile_form = UserProfileForm(instance=profile_user)
  
  context = {
     'form':form, 
     'profile_form':profile_form, 
     'view': 'update',
     'id' : id
     }
  return render(request, "users/crud_user_management.html", context)
      	
def DeleteUserManagementView(request, id):
    # Search user
    user = get_object_or_404(User, id=id)
    
    # search user either superuser or not
    if not request.user.is_superuser:
      messages.error(request, "You do not have permission to delete users.")
      return redirect('user_management_page')

    # cannot delete current user
    if user == request.user:
      messages.error(request, "You cannot delete yourself.")
      return redirect('user_management_page')

    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('user_management_page')
  
def DetailsUserManagementView(request,id):
  if request.user.is_authenticated:
    user_record = User.objects.get(id=id)
    user_profile_record = UserProfile.objects.get(user_id=id)
    context =  {
       'user_record':user_record, 
       'user_profile_record': user_profile_record, 
       'view':'details',
       'id':id
    }
    return render(request, 'users/crud_user_management.html',context)
  else:
    messages.success(request, "You Must Be Logged In To View That Page...")
    return redirect('login_page')
    