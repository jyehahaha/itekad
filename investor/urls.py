from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView, name='dashboard_page'),
]