from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login_page'),
    path('register/', views.RegisterView, name='register_page'),
    path('forgot-password/', views.ForgotPasswordView, name='forgot_password_page'),
    path('reset-password/', views.ResetPasswordView, name='reset_password_page'),
    path('success-password/', views.SuccessPasswordView, name='success_password_page'),
]