from django.shortcuts import render

# Create your views here.
def LoginView(request):
  context = {}
  return render(request, 'users/login.html', context)

def RegisterView(request):
  context = {}
  return render(request, 'users/register.html', context)

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
