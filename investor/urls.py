from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home_page'),
    path('profile/', views.ProfilePageView, name='profile_investor_page'),
    path('change-password/', views.ChangePasswordPageView, name='change_password_page'),
    path('gallery/', views.GalleryPageView, name='gallery_page'),
    path('report/', views.ReportPageView, name='report_page'),
]