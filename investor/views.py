from django.shortcuts import render

# Create your views here.
def LandingView(request):
    context = {}
    return render(request, 'investor/landing.html', context)

def HomePageView(request):
    context = {}
    return render(request, 'investor/home.html', context)

def ProfilePageView(request):
    context = {}
    return render(request, 'investor/profile.html', context)

def GalleryPageView(request):
    context = {}
    return render(request, 'investor/gallery.html', context)

def ReportPageView(request):
    context = {}
    return render(request, 'investor/report.html', context)