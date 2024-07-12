from django.shortcuts import render
from sfd.models import Campaign, CompanyProfile,TrancheInvestor, TrancheEntrepreneur

# Create your views here.
def LandingPageView(request):
	campaigns = Campaign.objects.all()
	context = {
		'title': 'Home',
		'landing': True,
		'campaign_info' : campaigns,
	}
	return render(request, 'website/landing.html', context)

def AboutPageView(request):
	context = {
		'title': 'About Us',
		'about': True,
	}
	return render(request, 'website/about.html', context)

def CampaignsPageView(request):
	campaigns = Campaign.objects.all()
	context = {
		'title': 'Campaigns',
		'campaigns': True,
		'campaigns' : campaigns,
	}
	return render(request, 'website/campaigns.html', context)


def CampaignsInfoPageView(request, id):
	campaign = Campaign.objects.get(id=id)
	company_profile = CompanyProfile.objects.all()
	investors = TrancheInvestor.objects.filter(campaign_id=campaign.id)
	Entrepreneurs = TrancheEntrepreneur.objects.filter(campaign_id=campaign.id)
	
	context = {
		'title': 'Campaigns',
		'campaign' : campaign,
		'investors' : investors,
		'Entrepreneurs' : Entrepreneurs,
		'company_profile' : company_profile,
	}
	return render(request, 'website/campaign_info.html', context)

def ContactPageView(request):
	context = {
		'title': 'Contact Us',
		'contact': True,
	}
	return render(request, 'website/contact.html', context)