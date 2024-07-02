from django.shortcuts import render,redirect
from .forms import CompanyProfileForm,CampaignForm,TrancheEntreprenuerForm,TrancheInvestorForm,TrancheReportForm,NatureOfBusinessForm,CategoryOfBusinessForm
from .models import CategoryOfBusiness,NatureOfBusiness,Campaign,CompanyProfile,TrancheEntreprenuer,TrancheInvestor,TrancheReport
from users.models import User,UserProfile
# Create your views here.


def DashboardView(request):
 
  investors = UserProfile.objects.filter(role='INVESTOR')
 
  totalInvestor = investors.count()
  totalCampaign = Campaign.objects.count()

  context = {
    'investors' : investors,
    'totalInvestor': totalInvestor,
    'totalCampaign': totalCampaign
  }
  return render(request, 'sfd/dashboard.html', context)

def BusinessProfileView(request):
  companies = CompanyProfile.objects.all()
  context = {
      'companies' : companies
  }
  return render(request, 'sfd/business.html', context)

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
  query = Campaign.objects.all()
  context = {
    'campaigns' : query
  }
  return render(request, 'sfd/campaign.html', context)

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
  entereprenuers_tranche = TrancheEntreprenuer.objects.filter(campaign__id=id)
  report_tranche = TrancheReport.objects.filter(campaign__id=id)

  context = {
    'view': 'assign',
    'campaign': campaign,
    'investors_tranche': investors_tranche,
    'entereprenuers_tranche': entereprenuers_tranche,
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

def EnterprenuerView(request, id):
  # fetch campaign
  campaign = Campaign.objects.get(id=id)
   # fetch entreprenuer assign
  e = TrancheEntreprenuer.objects.filter(campaign__id=id)

  # organize user id in list
  e_entreprenuer = []
  for x in e:
    e_entreprenuer.append(x.user.id)

  # fetch and exclude investor already assign
  entreprenuers = UserProfile.objects.filter(role='ENTREPRENEUR').exclude(id__in=e_entreprenuer)

  context = {
    'view': 'assign',
    'campaign': campaign,
    'entreprenuers': entreprenuers,
  }
  return render(request, 'sfd/crud_entreprenuer.html', context)

def CreateEnterprenuerView(request):
  # fetch campaign
  campaign = Campaign.objects.get(id=id)
  # fetch investor
  entreprenuer = UserProfile.objects.get(id=request.GET['user'])
  # form
  form = TrancheEntreprenuerForm({ 'campaign': campaign, 'user': entreprenuer })

    # form submit
  if request.method == "POST":
    form = TrancheEntreprenuerForm(request.POST)
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
  return render(request, 'sfd/crud_entreprenuer.html', context)

def UpdateEnterprenuerView(request):
  context = {}
  return render(request, 'sfd/crud_investor.html', context)

def DeleteEnterprenuerView(request,id):
  # Fetch entreprenuer tranche
  entreprenuer_tranche = TrancheEntreprenuer.objects.get(id=id)
  # Fetch campaign ID
  campaign = Campaign.objects.get(id=entreprenuer_tranche.campaign.id)

  if request.method == "POST":
    entreprenuer_tranche.delete()
    return redirect('assign_campaign_page', campaign.id)

  context = {
    'view': 'delete',
    'entreprenuer_tranche' : entreprenuer_tranche,
    'campaign': campaign,

  }
  return render(request, 'sfd/crud_investor.html', context)

def UploadReportView(request,id):
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