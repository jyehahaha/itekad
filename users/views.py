from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from .models import User, UserProfile
from .forms import UserForm, UserProfileForm, UserUpdateForm

# Create your views here.
def LoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile = UserProfile.objects.get(user=user)
            if profile.role == "INVESTOR":
                messages.success(request, ("You Have Been Logged In!"))
                return redirect('home_page')
            else:
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
	return redirect('landing_page')

def RegisterView(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    
    
    if form.is_valid():
      form.save()
      
      
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
			
      # log in user
			
      # log in user
      user = authenticate(username=username, password=password)
      login(request, user)


      messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
      return redirect('home_page')
      return redirect('home_page')
    else:
      messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
      return redirect('register_page')
  else:
    form = UserForm()
  
  return render(request, 'users/register.html', {'form':form})  
    form = UserForm()
  
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
        user_record = User.objects.all()
        user_profile_record = UserProfile.objects.all()
        return render(request, 'users/user_management.html', {'user_record':user_record, 'user_profile_record':user_profile_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('login_page')
    
def CreateUserManagementView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
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
    return render(request, 'users/crud_user_management.html', {'user_form': user_form, 'profile_form': profile_form, 'view': 'create'})

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

        current_user = User.objects.get(id=id or request.user.id)
        profile_user = UserProfile.objects.get(user__id=id or request.user.id)

      form = UserUpdateForm(instance=current_user)
      profile_form = UserProfileForm(instance=profile_user)
      return render(request, "users/crud_user_management.html", {'form':form, 'profile_form':profile_form, 'view': 'update'})
      	
def DeleteUserManagementView(request, id):
    
    user = get_object_or_404(User, id=id)
    
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete users.")
        return redirect('user_management_page')

    if user == request.user:
        messages.error(request, "You cannot delete yourself.")
        return redirect('user_management_page')

    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('user_management_page')


	# if request.user.is_authenticated:
	# 	delete_it = User.objects.get(id=id)
	# 	delete_it.delete()
	# 	messages.success(request, "Record Deleted Successfully...")
	# 	return render(request, 'users/crud_user_management.html')
	# else:
	# 	messages.success(request, "You Must Be Logged In To Do That...")
	# 	return redirect('user_management_page')
  
def DetailsUserManagementView(request,id):
    if request.user.is_authenticated:
        user_record = User.objects.get(id=id)
        user_profile_record = UserProfile.objects.get(user_id=id)
        return render(request, 'users/crud_user_management.html', {'user_record':user_record, 'user_profile_record': user_profile_record, 'view':'details'})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('login_page')
    

