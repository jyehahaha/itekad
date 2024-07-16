from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import (
  CompanyProfileForm,
  CampaignForm,
  TrancheEntrepreneurForm,
  TrancheInvestorForm,
  TrancheReportForm,
  NatureOfBusinessForm,
  CategoryOfBusinessForm,
)
from .models import (
  CategoryOfBusiness,
  NatureOfBusiness,
  Campaign,
  CompanyProfile,
  TrancheEntrepreneur,
  TrancheInvestor,
  TrancheReport,
)
from users.models import (
  User,
  UserProfile,
)
from users.forms import (
  UserForm,
  UserProfileForm,
  UserUpdateForm,
)
from users.filters import UserFilter
from django.core.paginator import (
  Paginator,
  EmptyPage,
  PageNotAnInteger,
)
from .filters import (
  CompanyFilter,
  CampaignFilter
)

# Create your views here.
@login_required
def DashboardView(request):
  # fetch investor
  investors = UserProfile.objects.filter(role='INVESTOR')
  campaigns = Campaign.objects.all()

  # get total
  totalInvestor = investors.count()
  totalCampaign = campaigns.count()

  context = {
    'investors' : investors,
    'totalInvestor': totalInvestor,
    'totalCampaign': totalCampaign
  }
  return render(request, 'sfd/dashboard.html', context)

@login_required
def UsersView(request):
  # fetch user profile
  records = UserProfile.objects.filter(user__is_superuser=False)

  # filter
  f = UserFilter(request.GET, queryset=records)

  # variable for paginator
  page_num = request.GET.get('page', 1)
  limit = request.GET.get('limit', 10)

  # pass the list for pagination
  paginator = Paginator(f.qs, limit)

  # paginator
  try:
    page_obj = paginator.page(page_num)
  except PageNotAnInteger:
    # if page is not an integer, deliver the first page
    page_obj = paginator.page(1)
  except EmptyPage:
    # if the page is out of range, deliver the last page
    page_obj = paginator.page(paginator.num_pages)

  context = {
    'view': 'list',
    'filter': f,
    'page_obj': page_obj,
  }
  return render(request, 'sfd/crud_user.html', context)

@login_required
def CreateUserView(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST)
    profile_form = UserProfileForm(request.POST)
    user_form.terms_agreement = True

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save(commit=False)
      user.save()
        
      try:
        profile = UserProfile.objects.get(user=user)
      except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

      # Update the profile fields from the form
      profile_form = UserProfileForm(request.POST, instance=profile)
      profile_form.save()

      return redirect('user_management_page')  # Redirect to the user management page after registration
  else:
    user_form = UserForm()
    profile_form = UserProfileForm()

  context = {
    'view': 'create',
    'form1': user_form,
    'form2': profile_form,
  }
  return render(request, 'sfd/crud_user.html', context)

@login_required
def UpdateUserView(request, id):
  # fetch user by id
  current_user = User.objects.get(id=id or request.user.id)
  # fetch user profile by id
  profile_user = UserProfile.objects.get(user__id=id or request.user.id)

  # get user form & assign instance
  form = UserUpdateForm(instance=current_user)
  # get user profile form & assign instance
  profile_form = UserProfileForm(instance=profile_user)

  # form method post
  if request.method == "POST":
    # Get Current User
    current_user = User.objects.get(id=id)
    # Get Current User's Profile
    profile_user = UserProfile.objects.get(user__id=id)

    form = UserUpdateForm(request.POST or None, instance=current_user)
    profile_form = UserProfileForm(request.POST or None, instance=profile_user)

    if form.is_valid() and profile_form.is_valid():
      form.save()
      profile_form.save()
      messages.success(request, "Your Info Has Been Updated!!")
      return redirect('user_management_page')
    else:
       print(form.errors)
       print(profile_form.errors)


  context = {
    'view': 'update',
    'id' : id,
    'form':form,
    'profile_form':profile_form,
  }
  return render(request, 'sfd/crud_user.html', context)

@login_required
def DeleteUserView(request, id):
  # Search user
  user = get_object_or_404(User, id=id)

  # search user either superuser or not
  if not request.user.is_superuser:
    messages.error(request, "You do not have permission to delete users.")
    return redirect('users_page')

  # cannot delete current user
  if user == request.user:
    messages.error(request, "You cannot delete yourself.")
    return redirect('users_page')

  user.delete()
  messages.success(request, "User deleted successfully.")
  return redirect('users_page')

  context = {
    'view': 'delete',
  }
  return render(request, 'sfd/crud_user.html', context)

@login_required
def DetailsUserView(request, id):
  user_record = User.objects.get(id=id)
  user_profile_record = UserProfile.objects.get(user_id=id)
  
  context = {
    'view':'details',
    'id':id,
    'user_record':user_record, 
    'user_profile_record': user_profile_record,
  }
  return render(request, 'sfd/crud_user.html', context)

def BusinessProfileView(request):
  if request.user.is_authenticated:
    # Look Up Records
    companies = CompanyProfile.objects.all()
    # user_profile_record = UserProfile.objects.filter(user__is_superuser=False)

    # filter
    f = CompanyFilter(request.GET, queryset=companies)

    # variable for paginator
    page_num = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    # pass the list for pagination
    paginator = Paginator(f.qs, limit)

    # paginator
    try:
      page_obj = paginator.page(page_num)
    except PageNotAnInteger:
      # if page is not an integer, deliver the first page
      page_obj = paginator.page(1)
    except EmptyPage:
      # if the page is out of range, deliver the last page
      page_obj = paginator.page(paginator.num_pages)

    context = {
      'filter': f,
      'page_obj': page_obj,
      'dashboard_view': True,
    }

    return render(request, 'sfd/business.html', context)
  else:
    messages.success(request, "You Must Be Logged In To View That Page...")
    return redirect('login_page')

def CreateBusinessProfileView(request):
  if request.method == "POST":
    form = CompanyProfileForm(request.POST)

    if form.is_valid():
      company = form.save(commit=False)
      company.status = True
      company.save()
      return redirect("business_profile_page")
  else:
    form = CompanyProfileForm()
    
  context = {
    'form': form,
    'view': 'create',
  }
  return render(request, 'sfd/crud_business.html', context)

def UpdateBusinessProfileView(request, id):
  company = CompanyProfile.objects.get(id=id)

  if request.method == "POST":
    form = CompanyProfileForm(request.POST, instance=company)

    if form.is_valid():
      form.save()
      return redirect("business_profile_page")
    
  else:
    form = CompanyProfileForm(instance=company)

  context = {
    'view': 'update',
    'form': form
  }
  return render(request, 'sfd/crud_business.html', context)

def DeleteBusinessProfileView(request, id):
  company = CompanyProfile.objects.get(id=id)

  if request.method == "POST":
    company.delete()
    return redirect("business_profile_page")
  
  context = {
    'view': 'delete',
    'company': company
  }
  return render(request, 'sfd/crud_business.html', context)

def DetailsBusinessProfileView(request, id):
  company = CompanyProfile.objects.get(id=id)
  context = {
    'view': 'details',
    'company': company
  }
  return render(request, 'sfd/crud_business.html', context)

def CategoryView(request):
  query = CategoryOfBusiness.objects.all()
  context = {
    'items' : query
  }
  return render(request, 'sfd/category.html', context)

def CreateCategoryView(request):
  if request.method == "POST":
    form = CategoryOfBusinessForm(request.POST)

    if form.is_valid():
      category = form.save(commit=False)
      category.status = True
      category.save()
      return redirect("category_page")
  else:
    form = CategoryOfBusinessForm()

  context = {
    'form': form,
    'view': 'create',
  }
  return render(request, 'sfd/crud_category.html', context)

def UpdateCategoryView(request, id):
  item = CategoryOfBusiness.objects.get(id=id)

  if request.method == "POST":
    form = CategoryOfBusinessForm(request.POST, instance=item)

    if form.is_valid():
      form.save()
      return redirect("category_page")
  else:
    form = CategoryOfBusinessForm(instance=item)

  context = {
    'view': 'update',
    'form': form
  }
  return render(request, 'sfd/crud_category.html', context)

def DeleteCategoryView(request, id):
  item = CategoryOfBusiness.objects.get(id=id)

  if request.method == "POST":
    item.delete()
    return redirect("category_page")
  
  context = {
    'view': 'delete',
    'item': item
  }
  return render(request, 'sfd/crud_category.html', context)

def DetailsCategoryView(request, id):
  item = CategoryOfBusiness.objects.get(id=id)
  context = {
    'view' : 'details',
    'item' : item
  }
  return render(request, 'sfd/crud_category.html', context)

def NatureBusinessView(request):
  query = NatureOfBusiness.objects.all()
  context = {
    'items' : query
  }
  return render(request, 'sfd/nature_business.html', context)

def CreateNatureView(request):
  if request.method == "POST":
    form = NatureOfBusinessForm(request.POST)

    if form.is_valid():
      item = form.save(commit=False)
      item.status = True
      item.save()
      return redirect("nature_of_business_page")
  else:
    form = NatureOfBusinessForm()

  context = {
    'form': form,
    'view': 'create'
  }
  return render(request, 'sfd/crud_nature_business.html', context)

def UpdateNatureView(request, id):
    item = NatureOfBusiness.objects.get(id=id)

    if request.method == "POST":
      form = NatureOfBusinessForm(request.POST, instance=item)

      if form.is_valid():
        form.save()
        return redirect("nature_of_business_page")
    else:
      form = NatureOfBusinessForm(instance=item)
  
    context = {
      'view': 'update',
      'form': form
    }
    return render(request, 'sfd/crud_nature_business.html', context)

def DeleteNatureView(request, id):
    item = NatureOfBusiness.objects.get(id=id)

    if request.method == "POST":
      item.delete()
      return redirect("nature_of_business_page")

    context = {
      'view': 'delete',
       'item': item
    }
    return render(request, 'sfd/crud_nature_business.html', context)

def DetailsNatureView(request, id):
  item = NatureOfBusiness.objects.get(id=id)
  context = {
    'view': 'details',
    'item' : item
  }
  return render(request, 'sfd/crud_nature_business.html', context)

def CampaignView(request):
  if request.user.is_authenticated:
    # Look Up Records
    query = Campaign.objects.all()

    # filter
    f = CampaignFilter(request.GET, queryset=query)

    # variable for paginator
    page_num = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    # pass the list for pagination
    paginator = Paginator(f.qs, limit)

    # paginator
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
      'filter': f,
      'page_obj': page_obj,
      'dashboard_view': True,
    }

    return render(request, 'sfd/campaign.html', context)
  else:
    messages.success(request, "You Must Be Logged In To View That Page...")
    return redirect('login_page')

def CreateCampaignView(request):
  if request.method == "POST":
    form = CampaignForm(request.POST)

    if form.is_valid():
      campaign = form.save(commit=False)
      campaign.status = True
      campaign.save()
      return redirect("campaign_page")
  else:
    form = CampaignForm()

  context = {
    'form': form,
    'view': 'create'
  }
  return render(request, 'sfd/crud_campaign.html', context)

def UpdateCampaignView(request, id):
  campaign = Campaign.objects.get(id=id)

  if request.method == "POST":
    form = CampaignForm(request.POST, instance=campaign)

    if form.is_valid():
      form.save()
      return redirect("campaign_page")
  
  else:
    form = CampaignForm(instance=campaign)

  context = {
    'view': 'update',
    'form': form
  }
  return render(request, 'sfd/crud_campaign.html', context)

def DeleteCampaignView(request, id):
  campaign = Campaign.objects.get(id=id)

  if request.method == "POST":
      campaign.delete()
      return redirect("campaign_page")

  context = {
    'view': 'delete',
    'campaign': campaign
  }
  return render(request, 'sfd/crud_campaign.html', context)

def DetailsCampaignView(request, id):
  campaign = Campaign.objects.get(id=id)
  context = {
    'view': 'details',
    'campaign' : campaign
  }
  return render(request, 'sfd/crud_campaign.html', context)

def AssignCampaignView(request, id):
  campaign = Campaign.objects.get(id=id)
  investors_tranche = TrancheInvestor.objects.filter(campaign__id=id)
  entrepreneurs_tranche = TrancheEntrepreneur.objects.filter(campaign__id=id)
  report_tranche = TrancheReport.objects.filter(campaign__id=id)

  context = {
    'view': 'assign',
    'campaign': campaign,
    'investors_tranche': investors_tranche,
    'entrepreneurs_tranche': entrepreneurs_tranche,
    'report_tranche': report_tranche
  }
  return render(request, 'sfd/assign_page.html', context)

def InvestorView(request, id):
  # fetch campaign
  campaign = Campaign.objects.get(id=id)
  # fetch investors assign
  t = TrancheInvestor.objects.filter(campaign__id=id)

  # organize user id in list
  t_investors = []
  for x in t:
    t_investors.append(x.user.id)

  # fetch and exclude investor already assign
  investors = UserProfile.objects.filter(role="INVESTOR").exclude(id__in=t_investors)

  context = {
    'view': 'assign',
    'campaign': campaign,
    'investors': investors,
  }
  return render(request, 'sfd/crud_investor.html', context)

def CreateInvestorView(request, id):
  # fetch campaign
  campaign = Campaign.objects.get(id=id)
  # fetch investor
  investor = UserProfile.objects.get(id=request.GET['user'])
  # form
  form = TrancheInvestorForm({ 'campaign': campaign, 'user': investor })
  
  # form submit
  if request.method == "POST":
    form = TrancheInvestorForm(request.POST)
    #  form valid
    if form.is_valid():
      # form save
      form.save()
      return redirect('assign_campaign_page', campaign.id)

  context = {
    'view': 'create',
    'form': form,
    'campaign': campaign,
  }
  return render(request, 'sfd/crud_investor.html', context)

def UpdateInvestorView(request):
  context = {

  }
  return render(request, 'sfd/crud_investor.html', context)

def DeleteInvestorView(request,id):
  investors_tranche = TrancheInvestor.objects.get(id=id)
  campaign = Campaign.objects.get(id=investors_tranche.campaign.id)

  if request.method == "POST":
    investors_tranche.delete()
    return redirect('assign_campaign_page', campaign.id)

  context = {
    'view': 'delete',
    'investors_tranche' : investors_tranche,
    'campaign': campaign,
  }
  return render(request, 'sfd/crud_investor.html', context)

def EntrepreneurView(request, id):
  # fetch campaign
  campaign = Campaign.objects.get(id=id)
   # fetch Entrepreneur assign
  e = TrancheEntrepreneur.objects.filter(campaign__id=id)

  # organize user id in list
  e_Entrepreneur = []
  for x in e:
    e_Entrepreneur.append(x.user.id)

  # fetch and exclude investor already assign
  Entrepreneurs = UserProfile.objects.filter(role='ENTREPRENEUR').exclude(id__in=e_Entrepreneur)

  context = {
    'view': 'assign',
    'campaign': campaign,
    'Entrepreneurs': Entrepreneurs,
  }
  return render(request, 'sfd/crud_Entrepreneur.html', context)

def CreateEntrepreneurView(request):
  # fetch campaign
  campaign = Campaign.objects.get(id=id)
  # fetch investor
  Entrepreneur = UserProfile.objects.get(id=request.GET['user'])
  # form
  form = TrancheEntrepreneurForm({ 'campaign': campaign, 'user': Entrepreneur })

    # form submit
  if request.method == "POST":
    form = TrancheEntrepreneurForm(request.POST)
    #  form valid
    if form.is_valid():
      # form save
      form.save()
      return redirect('assign_campaign_page', campaign.id)

  context = {
    'view': 'create',
    'form': form,
    'campaign': campaign,

  }
  return render(request, 'sfd/crud_Entrepreneur.html', context)

def UpdateEntrepreneurView(request):
  context = {}
  return render(request, 'sfd/crud_investor.html', context)

def DeleteEntrepreneurView(request,id):
  # Fetch Entrepreneur tranche
  Entrepreneur_tranche = TrancheEntrepreneur.objects.get(id=id)
  # Fetch campaign ID
  campaign = Campaign.objects.get(id=Entrepreneur_tranche.campaign.id)

  if request.method == "POST":
    Entrepreneur_tranche.delete()
    return redirect('assign_campaign_page', campaign.id)

  context = {
    'view': 'delete',
    'Entrepreneur_tranche' : Entrepreneur_tranche,
    'campaign': campaign,

  }
  return render(request, 'sfd/crud_investor.html', context)

def UploadReportView(request):
  context = {}
  return render(request, 'sfd/assign_page.html', context)

def CreateReportView(request,id):
  # fetch campaign
  campaign = Campaign.objects.get(id=id)
  # form
  form = TrancheReportForm({ 'campaign': campaign })

  # form submit
  if request.method == "POST":
    form = TrancheReportForm(request.POST)
    #  form valid
    if form.is_valid():
      # form save
      form.save()
      return redirect('assign_campaign_page', campaign.id)

  context = {
    'view': 'create',
    'form': form,
    'campaign': campaign, 
  }
  return render(request, 'sfd/crud_report.html', context)

def UpdateReportView(request,campaign, id):
  #fetch campaign
  campaign = Campaign.objects.get(id=campaign)
  # fetch report
  report = TrancheReport.objects.get(id=id)
  # fetch report 
  form = TrancheReportForm(instance=report)

  if request.method == "POST":
    form = TrancheReportForm(request.POST, instance=report)

    if form.is_valid():
      form.save()
      return redirect("assign_campaign_page",campaign.id)

  context = {
    'view': 'update',
    'form': form,
    'campaign': campaign
  }
  
  return render(request, 'sfd/crud_report.html', context)

def DeleteReportView(request,id):
    # Fetch report tranche
  report_tranche = TrancheReport.objects.get(id=id)
    # Fetch campaign ID
  campaign = Campaign.objects.get(id=report_tranche.campaign.id)

  if request.method == "POST":
    report_tranche.delete()
    return redirect('assign_campaign_page', campaign.id)

  context = {
    'view': 'delete',
    'report_tranche' : report_tranche,
    'campaign': campaign,
  }
  return render(request, 'sfd/crud_report.html', context)
