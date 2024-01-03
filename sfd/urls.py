from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView, name='dashboard_page'),
    path('tranche/', views.TrancheView, name='tranche_page'),
    path('tranche/create/', views.CreateTrancheView, name='create_tranche_page'),
    path('tranche/update/<int:id>/', views.UpdateTrancheView, name='update_tranche_page'),
    path('tranche/delete/<int:id>/', views.DeleteTrancheView, name='delete_tranche_page'),
    path('tranche/details/<int:id>/', views.DetailsTrancheView, name='details_tranche_page'),
    path('business/', views.BusinessProfileView, name='business_profile_page'),
    path('business/create/', views.CreateBusinessProfileView, name='create_business_profile_page'),
    path('business/update/<int:id>/', views.UpdateBusinessProfileView, name='update_business_profile_page'),
    path('business/delete/<int:id>/', views.DeleteBusinessProfileView, name='delete_business_profile_page'),
    path('business/details/<int:id>/', views.DetailsBusinessProfileView, name='details_business_profile_page'),
    path('report/', views.UploadReportView, name='upload_report_page'),
    path('category/', views.CategoryView, name='category_page'),
    path('category/create/', views.CreateCategoryView, name='create_category_page'),
    path('category/update/<int:id>/', views.UpdateCategoryView, name='update_category_page'),
    path('category/delete/<int:id>/', views.DeleteCategoryView, name='delete_category_page'),
    path('category/details/<int:id>/', views.DetailsCategoryView, name='details_category_page'),
    path('nature/', views.NatureBusinessView, name='nature_of_business_page'),
    path('nature/create/', views.CreateNatureView, name='create_nature_of_business_page'),
    path('nature/update/<int:id>/', views.UpdateNatureView, name='update_nature_of_business_page'),
    path('nature/delete/<int:id>/', views.DeleteNatureView, name='delete_nature_of_business_page'),
    path('nature/details/<int:id>/', views.DetailsNatureView, name='details_nature_of_business_page'),
    path('campaign/', views.CampaignView, name='campaign_page'),
    path('campaign/create/', views.CreateCampaignView, name='create_campaign_page'),
    path('campaign/update/<int:id>/', views.UpdateCampaignView, name='update_campaign_page'),
    path('campaign/delete/<int:id>/', views.DeleteCampaignView, name='delete_campaign_page'),
    path('campaign/details/<int:id>/', views.DetailsCampaignView, name='details_campaign_page'),
    path('campaign/assign/<int:id>/', views.AssignInvestorCampaignView, name='assign_investor_campaign_page'),



]