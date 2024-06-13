import django_filters as filters
from django import forms
from users.models import *

class ApplicantFilter(filters.FilterSet):
  name = filters.CharFilter(field_name='get_full_name', label='Customer Name', lookup_expr='icontains')
  mykad_no = filters.NumberFilter(field_name='user__mykad_no', label='Mykad No.', lookup_expr='icontains')
  username = filters.CharFilter(field_name='username', label='Customer Name', lookup_expr='icontains')
  email = filters.CharFilter(field_name='email', label='Email', lookup_expr='icontains')
  bank_account_number = filters.CharFilter(field_name='user__bank_account_number', label='Account No.', lookup_expr='exact')
  bank_name = filters.CharFilter(field_name='user__bank_name', label='Bank Name', lookup_expr='exact')
  start_date = filters.DateFilter(field_name='last_modified', label='Start Date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = filters.DateFilter(field_name='last_modified', label='End Date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}))
  status = filters.ModelChoiceFilter(field_name='is_active', label='Status', lookup_expr='exact')
  role = filters.ChoiceFilter(choices=User.role.choice, label='Role', lookup_expr='exact')
  category = filters.ModelChoiceFilter(choices=User.position.choice, label='Category', method='exact')

  class Meta:
    model = User
    fields = {}