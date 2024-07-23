from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import (
	User,
	UserProfile,
)
from users.forms import (
	UserForm,
	UserProfileForm,
)
from sfd.models import (
	TrancheInvestor,
)
def approved_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.userprofile.is_approved:
            return redirect('wait_for_approval_page')  # Redirect to a page that informs the user to wait for approval
        return view_func(request, *args, **kwargs)
    return wrapper

# Create your views here.
def LandingView(request):
	context = {}
	return render(request, 'investor/landing.html', context)

@approved_required
@login_required(login_url='login_page')
def HomePageView(request):
	if request.user.is_authenticated:
		user = UserProfile.objects.get(user__id = request.user.id)

	context = {
		'user' : user,
	}
	return render(request, 'investor/home.html', context)

@login_required(login_url='login_page')
def ProfilePageView(request):
	# search user profile by id
	profile = UserProfile.objects.get(user__id=request.user.id)

	if request.method == 'POST':
		form = UserProfileForm(request.POST,instance=profile)
		if form.is_valid():
			investor = form.save()
			investor.is_edited = False  # Set is_edited to False
			investor.save()  # Save the updated profile
			update_session_auth_hash(request, investor)  # Important!
			messages.success(request, 'Your profile was successfully updated!')
			return redirect('home_page')
	else:
		form = UserProfileForm(instance=profile)

	context = {
		'form' : form
	}
	return render(request, 'investor/profile.html', context)

@login_required(login_url='login_page')
def ChangePasswordPageView(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('home_page')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)

	context = {
		'form' : form,
	}
	return render(request, 'investor/change_password.html', context)

@login_required(login_url='login_page')
def CampaignInvestorPageView(request):
	# search campaign which investor invest
	campaigns = TrancheInvestor.objects.filter(user__user__id=request.user.id)
	context = {
		'campaigns': campaigns,
	}
	return render(request, 'investor/campaigns.html', context)

@login_required(login_url='login_page')
def GalleryPageView(request):
	context = {}
	return render(request, 'investor/gallery.html', context)

@login_required(login_url='login_page')
def ReportPageView(request):
	context = {}
	return render(request, 'investor/report.html', context)

def wait_for_approval_page(request):
    return render(request, 'investor/wait_for_approval.html')