from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

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
