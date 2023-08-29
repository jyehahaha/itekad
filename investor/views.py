from django.shortcuts import render

# Create your views here.
def LandingView(request):
    context = {}
    return render(request, 'investor/landing.html', context)

def DashboardView(request):
    context = {}
    return render(request, 'investor/dashboard.html', context)