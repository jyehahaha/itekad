from django.shortcuts import render

# Create your views here.
def DashboardPageView(request):
    context = {}
    return render(request, 'investor/dashboard.html', context)