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