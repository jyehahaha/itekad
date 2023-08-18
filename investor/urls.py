from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardPageView, name='dashboard_page'),
]