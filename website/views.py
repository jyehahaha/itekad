from django.shortcuts import render

# Create your views here.
def LandingPageView(request):
    context = {}
    return render(request, 'website/landing.html', context)