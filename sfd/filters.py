import django_filters as filters
from django import forms
from sfd.models import *

class CompanyFilter(filters.FilterSet):
  company_name = filters.CharFilter(field_name='company_name', label='Company Name', lookup_expr='icontains')
  company_registration_number = filters.CharFilter(field_name='company_registration_number', label='Business Registration Number', lookup_expr='icontains')
  start_date = filters.DateFilter(field_name='created_at', label='Start Date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = filters.DateFilter(field_name='created_at', label='End Date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}))
  status = filters.ChoiceFilter(choices=((True, 'Active'), (False, 'Inactive')), field_name='company_status', label='Status', lookup_expr='exact')

  class Meta:
    model = CompanyProfile
    fields = ['company_name', 'company_registration_number', 'start_date', 'end_date', 'status']

class CampaignFilter(filters.FilterSet):
  # business_profile_id = filters.CharFilter(field_name='companyprofileid', label='Business Profile ID', lookup_expr='exact')
  title = filters.CharFilter(field_name='title', label='Title', lookup_expr='icontains')
  start_date = filters.DateFilter(field_name='start_campaign', label='Start Campaign Date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = filters.DateFilter(field_name='end_campaign', label='End Campaign Date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}))
  status = filters.ChoiceFilter(choices=((True, 'Active'), (False, 'Inactive')), field_name='status', label='Status', lookup_expr='exact')

  class Meta:
    model = Campaign
    fields = ['title', 'start_date', 'end_date', 'status']
