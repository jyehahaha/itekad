from django.shortcuts import render

# Create your views here.


def DashboardView(request):
  context = {}
  return render(request, 'sfd/dashboard.html', context)

def BusinessProfileView(request):
  context = {}
  return render(request, 'sfd/business.html', context)

def CreateBusinessProfileView(request):
  context = {
    'view': 'create',
  }
  return render(request, 'sfd/crud_business.html', context)

def UpdateBusinessProfileView(request, id):
  # search by id
  # insert into form
  context = {
    'view': 'update',
  }
  return render(request, 'sfd/crud_business.html', context)

def DeleteBusinessProfileView(request, id):
  context = {
    'view': 'delete',
  }
  return render(request, 'sfd/crud_business.html', context)

def DetailsBusinessProfileView(request, id):
  context = {
    'view': 'details',
  }
  return render(request, 'sfd/crud_business.html', context)

def UploadReportView(request):
  context = {}
  return render(request, 'sfd/report.html', context)

def CategoryView(request):
  context = {
     'view': 'create',
  }
  return render(request, 'sfd/category.html', context)

def CreateCategoryView(request):
  context = {
    'view': 'create',
  }
  return render(request, 'sfd/crud_category.html', context)

def UpdateCategoryView(request, id):
  context = {
    'view': 'update',
  }
  return render(request, 'sfd/crud_category.html', context)

def DeleteCategoryView(request, id):
  context = {
    'view': 'delete',
  }
  return render(request, 'sfd/crud_category.html', context)

def DetailsCategoryView(request, id):
  context = {
    'view': 'details',
  }
  return render(request, 'sfd/crud_category.html', context)

def NatureBusinessView(request):
  context = {}
  return render(request, 'sfd/nature_business.html', context)


def CreateNatureView(request):
  context = {
    'view': 'create',
  }
  return render(request, 'sfd/crud_nature_business.html', context)

def UpdateNatureView(request, id):
  context = {
    'view': 'update',
  }
  return render(request, 'sfd/crud_nature_business.html', context)

def DeleteNatureView(request, id):
  context = {
    'view': 'delete',
  }
  return render(request, 'sfd/crud_nature_business.html', context)

def DetailsNatureView(request, id):
  context = {
    'view': 'details',
  }
  return render(request, 'sfd/crud_nature_business.html', context)

def CampaignView(request):
  context = {}
  return render(request, 'sfd/campaign.html', context)


def CreateCampaignView(request):
  context = {
    'view': 'create',
  }
  return render(request, 'sfd/crud_campaign.html', context)

def UpdateCampaignView(request, id):
  context = {
    'view': 'update',
  }
  return render(request, 'sfd/crud_campaign.html', context)

def DeleteCampaignView(request, id):
  context = {
    'view': 'delete',
  }
  return render(request, 'sfd/crud_campaign.html', context)

def DetailsCampaignView(request, id):
  context = {
    'view': 'details',
  }
  return render(request, 'sfd/crud_campaign.html', context)

def AssignInvestorCampaignView(request, id):
  context = {
    'view': 'assign',
  }
  return render(request, 'sfd/crud_campaign.html', context)

