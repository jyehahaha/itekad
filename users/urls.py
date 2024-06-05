from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login_page'),
    path('register/', views.RegisterView, name='register_page'),
    path('forgot-password/', views.ForgotPasswordView, name='forgot_password_page'),
    path('reset-password/', views.ResetPasswordView, name='reset_password_page'),
    path('success-password/', views.SuccessPasswordView, name='success_password_page'),
    path('user-management/', views.EnableDisableView, name='enable_disable_page'),
    path('send-password/', views.SendPassword, name='send_password_page'),
    path('user/', views.UserManagementView, name='user_management_page'),
    path('user/create/', views.CreateUserManagementView, name='create_user_management_page'),
    path('user/update/<int:id>/', views.UpdateUserManagementView, name='update_user_management_page'),
    path('user/delete/<int:id>/', views.DeleteUserManagementView, name='delete_user_management_page'),
    path('user/details/<int:id>/', views.DetailsUserManagementView, name='details_user_management_page'),
]