from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import User, UserProfile

User = get_user_model()

# Create your forms here.
class UserLoginForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ['username', 'password']

class UserForm(UserCreationForm):
	terms_agreement = forms.BooleanField(label='I accept all Privacy and Policy & Terms and Conditions.')
	class Meta:
		model = User
		fields = (
			"username",
			"first_name",
			"last_name",
			"email",
			"password1",
			"password2",
			"terms_agreement",
		)

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = (
			"first_name",
			"last_name",
			"email",
		)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = (
			"mykad_no",
			"mobile_no", 
			"country" , 
			"postcode",
			"address_line_one",
			"address_line_two",
			"address_line_three", 
			"city",
			"state",
			"bank_name",
			"bank_account_number",
			"role",
			"position"
		)
		labels = {
			'address_line_one': "Address 1",
			'address_line_two': "Address 2",
			'address_line_three': "Address 3",
		}

class CustomPasswordResetForm(PasswordResetForm):
	def save(self, *args, **kwargs):
		email = self.cleaned_data["email"]
		users = User.objects.filter(email=email)
		if not users.exists():
			raise forms.ValidationError("There is no user registered with the specified email address.")
		else:
			for user in users:
				user.userprofile.password_reset_timestamp = timezone.now()
				user.userprofile.save()
		super().save(*args, **kwargs)  