from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
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
         
        if user.is_active:
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
        else:
          messages.error(request, "Your account is not activated. Please check your email for activation instructions.")

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
      user.is_active = False
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

      # Generate token for email confirmation
      token = default_token_generator.make_token(user)

      # Send email verification
      current_site = get_current_site(request)
      mail_subject = 'Activate your account'
      message = render_to_string('users/activation_email.html', {
          'user': user,
          'domain': current_site.domain,
          'uid': urlsafe_base64_encode(force_bytes(user.pk)),
          'token': token,
      })
      
      to_email = form.cleaned_data.get('email')
      send_mail(mail_subject, message, 'from@example.com', [to_email])

      messages.success(request, f"Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
      return redirect('login_page')  # Redirect to login page after registration

    else:
      messages.success(request, "Whoops! There was a problem Registering, please try again...")
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

@login_required
def UserManagementView(request):
  # Look Up Records
  records = UserProfile.objects.filter(user__is_superuser=False)

  # filter
  f = UserFilter(request.GET, queryset=records)

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
  }

  return render(request, 'users/user_management.html', context)
    
@login_required
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

@login_required
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

@login_required
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

@login_required
def DetailsUserManagementView(request,id):
  user_record = User.objects.get(id=id)
  user_profile_record = UserProfile.objects.get(user_id=id)
  context =  {
      'user_record':user_record, 
      'user_profile_record': user_profile_record, 
      'view':'details',
      'id':id
  }
  return render(request, 'users/crud_user_management.html',context)
  
def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Your account has been activated.')
        return redirect('home_page')  # Redirect to home page or any desired page after activation
    else:
        messages.error(request, 'Activation link is invalid.')
        return redirect('login_page')  # Redirect to login page if activation fails
    