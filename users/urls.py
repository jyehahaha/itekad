from django.urls import path
from . import views
from .forms import CustomPasswordResetForm

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('login/', views.LoginView, name='login_page'),
    path('logout/', views.LogoutView, name='logout_page'),
    path('register/', views.RegisterView, name='register_page'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html', form_class=CustomPasswordResetForm), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('user-management/', views.EnableDisableView, name='enable_disable_page'),
    path('send-password/<int:id>/', views.SendPassword, name='send_password_page'),
    path('user/', views.UserManagementView, name='user_management_page'),
    path('user/create/', views.CreateUserManagementView, name='create_user_management_page'),
    path('user/update/<int:id>/', views.UpdateUserManagementView, name='update_user_management_page'),
    path('user/delete/<int:id>/', views.DeleteUserManagementView, name='delete_user_management_page'),
    path('user/details/<int:id>/', views.DetailsUserManagementView, name='details_user_management_page'),
    path('activate/<str:uidb64>/<str:token>/', views.activate_account, name='activate_account'),
]