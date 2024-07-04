import django_filters as filters
from django import forms
from users.models import *

class UserFilter(filters.FilterSet):
  firstname = filters.CharFilter(field_name='user__first_name', label='First Name', lookup_expr='icontains')
  lastname = filters.CharFilter(field_name='user__last_name', label='Last Name', lookup_expr='icontains')
  mykad_no = filters.NumberFilter(field_name='mykad_no', label='MyKad No.', lookup_expr='exact')
  username = filters.CharFilter(field_name='user__username', label='Staff ID', lookup_expr='icontains')
  email = filters.CharFilter(field_name='user__email', label='Email', lookup_expr='icontains')
  bank_account_number = filters.CharFilter(field_name='bank_account_number', label='Bank Account No.', lookup_expr='exact')
  bank_name = filters.CharFilter(field_name='bank_name', label='Bank Name', lookup_expr='exact')
  start_date = filters.DateFilter(field_name='user__date_joined', label='Start Date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = filters.DateFilter(field_name='user__date_joined', label='End Date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}))
  status = filters.ChoiceFilter(choices=((True, 'Active'), (False, 'Inactive')), field_name='user__is_active', label='Status', lookup_expr='exact')
  role = filters.ChoiceFilter(choices=UserProfile.Role.choices, label='Role', lookup_expr='iexact')
  position = filters.ChoiceFilter(choices=UserProfile.Position.choices, label='Position', lookup_expr='iexact')

  class Meta:
    model = UserProfile
    fields = ['firstname', 'lastname', 'username', 'mykad_no', 'bank_account_number', 'bank_name', 'role', 'position', 'username', 'email']
