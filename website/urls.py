from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView, name='landing_page'),
    path('about/', views.AboutPageView, name='about_page'),
    path('campaigns/', views.CampaignsPageView, name='campaigns_page'),
    path('campaign_info/<int:id>/', views.CampaignsInfoPageView, name='campaign_info'),
    path('contact/', views.ContactPageView, name='contact_page'),
]