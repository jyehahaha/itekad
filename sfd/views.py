from django.shortcuts import render,redirect
from .forms import CompanyProfileForm,CampaignForm,TrancheEntreprenuerForm,TrancheInvestorForm,TrancheReportForm,NatureOfBusinessForm,CategoryOfBusinessForm
from .models import CategoryOfBusiness,NatureOfBusiness,Campaign,CompanyProfile
# Create your views here.


def DashboardView(request):
  context = {}
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

def UploadReportView(request):
  context = {}
  return render(request, 'sfd/report.html', context)

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

def AssignInvestorCampaignView(request, id):
  context = {
    'view': 'assign',
  }
  return render(request, 'sfd/crud_campaign.html', context)

