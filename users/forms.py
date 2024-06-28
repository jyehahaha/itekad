from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from .models import User, UserProfile
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class UserForm(UserCreationForm):
    terms_agreement = forms.BooleanField(label='I accept all Privacy and Policy & Terms and Conditions.')
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "terms_agreement")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("mykad_no", "mobile_no", "country" , "postcode", "address_line_one", "address_line_two", "address_line_three", "city", "state", "bank_name", "bank_account_number", "role", "position")
        labels = {
            'address_line_one': "Address 1",
            'address_line_two': "Address 2",
            'address_line_three': "Address 3",
        }

class CustomPasswordResetForm(PasswordResetForm):
    def save(self, *args, **kwargs):
        email = self.cleaned_data["email"]
        users = User.objects.filter(email=email)
        for user in users:
            user.userprofile.password_reset_timestamp = timezone.now()
            user.userprofile.save()
        super().save(*args, **kwargs)  