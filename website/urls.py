from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView, name='landing_page'),
]