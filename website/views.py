from django.shortcuts import render

# Create your views here.
def LandingPageView(request):
    context = {
        'title': 'Home',
        'landing': True,
    }
    return render(request, 'website/landing.html', context)

def AboutPageView(request):
    context = {
        'title': 'About Us',
        'about': True,
    }
    return render(request, 'website/about.html', context)

def CampaignsPageView(request):
    context = {
        'title': 'Campaigns',
        'campaigns': True,
    }
    return render(request, 'website/campaigns.html', context)

def ContactPageView(request):
    context = {
        'title': 'Contact Us',
        'contact': True,
    }
    return render(request, 'website/contact.html', context)