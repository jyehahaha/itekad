from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.utils import timezone

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from django.contrib.auth import get_user_model
from .models import User, UserProfile

User = get_user_model()

# Create your forms here.
class UserLoginForm(AuthenticationForm):
	remember = forms.BooleanField(label="Remember me", required=False)
	class Meta:
		model = User
		fields = (
			'username',
			'password',
			'remember',
		)

class UserForm(UserCreationForm):
	terms_agreement = forms.BooleanField(label='I accept all Privacy and Policy & Terms and Conditions.')
	helper = FormHelper()
	helper.form_tag = False
	helper.layout = Layout(
		Div(
			Div(FieldWithButtons('password1',StrictButton('<i class="fa-solid fa-eye"></i>', type='button', css_class='btn btn-outline-secondary', id='password1Button')), css_class='col-12'),
			Div(FieldWithButtons('password2', StrictButton('<i class="fa-solid fa-eye"></i>', type='button', css_class='btn btn-outline-secondary', id='password2Button')), css_class='col-12'),
			css_class='row'
		)
	)
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
		labels = {
			"first_name": "First Name",
			"last_name": "Last Name",
			"email": "Email Address",
		}

	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(UserForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = (
			"first_name",
			"last_name",
			"email",
		)
		labels = {
			"first_name": "First Name",
			"last_name": "Last Name",
			"email": "Email Address",
		}

	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(UserUpdateForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = (
			"mykad_no",
			"mobile_no",
			"address_line_one",
			"address_line_two",
			"address_line_three", 
			"city",
			"postcode",
			"state",
			"country",
			"bank_name",
			"bank_account_number",
			"role",
			"position",
		)
		labels = {
			"mykad_no": "MyKad No. / Identification No.",
			"mobile_no": "Mobile No.",
			"address_line_one": "Address Line 1",
			"address_line_two": "Address Line 2",
			"address_line_three": "Address Line 3",
			"bank_name": "Bank Name",
			"bank_account_number": "Bank Account No.",
		}
		widgets = {
			"mykad_no": forms.TextInput(attrs={"required": "true"}),
		}

	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(UserProfileForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['mykad_no'].required = True
		self.fields['mobile_no'].required = True
		self.fields['address_line_one'].required = True
		self.fields['address_line_two'].required = True
		self.fields['city'].required = True
		self.fields['postcode'].required = True
		self.fields['state'].required = True
		self.fields['country'].required = True
		self.fields['bank_name'].required = True
		self.fields['bank_account_number'].required = True
		self.fields['role'].required = True
		self.fields['position'].required = True

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
