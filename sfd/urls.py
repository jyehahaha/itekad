from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView, name='dashboard_page'),
    path('users/', views.UsersView, name='users_page'),
    path('users/create/', views.CreateUserView, name='create_user_page'),
    path('users/update/<int:id>/', views.UpdateUserView, name='update_user_page'),
    path('users/delete/<int:id>/', views.DeleteUserView, name='delete_user_page'),
    path('users/details/<int:id>/', views.DetailsUserView, name='details_user_page'),
    path('business/', views.BusinessProfileView, name='business_profile_page'),
    path('business/create/', views.CreateBusinessProfileView, name='create_business_profile_page'),
    path('business/update/<int:id>/', views.UpdateBusinessProfileView, name='update_business_profile_page'),
    path('business/delete/<int:id>/', views.DeleteBusinessProfileView, name='delete_business_profile_page'),
    path('business/details/<int:id>/', views.DetailsBusinessProfileView, name='details_business_profile_page'),
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
    path('campaign/assign/<int:id>/', views.AssignCampaignView, name='assign_campaign_page'),
    path('investor/<int:id>/', views.InvestorView, name='investor_page'),
    path('investor/create/<int:id>/', views.CreateInvestorView, name='create_investor_page'),
    path('investor/update/<int:id>/', views.UpdateInvestorView, name='update_investor_page'),
    path('investor/delete/<int:id>/', views.DeleteInvestorView, name='delete_investor_page'),
    path('entrepreneur/<int:id>/', views.EntrepreneurView, name='entrepreneur_page'),
    path('entrepreneur/create/', views.CreateEntrepreneurView, name='create_entrepreneur_page'),
    path('entrepreneur/update/<int:id>/', views.UpdateEntrepreneurView, name='update_entrepreneur_page'),
    path('entrepreneur/delete/<int:id>/', views.DeleteEntrepreneurView, name='delete_entrepreneur_page'),
    path('report/', views.UploadReportView, name='upload_report_page'),
    path('report/create/<int:id>/', views.CreateReportView, name='create_report_page'),
    path('report/update/<int:campaign>/<int:id>/', views.UpdateReportView, name='update_report_page'),
    path('report/delete/<int:id>/', views.DeleteReportView, name='delete_report_page'),
]