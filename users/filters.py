import django_filters as filters
from django import forms
from Application.models import *

class ApplicantFilter(filters.FilterSet):
  name = filters.CharFilter(field_name='user__name', label='Customer Name', lookup_expr='icontains')
  mykad = filters.NumberFilter(field_name='user__mykad', label='Customer MyKad No.', lookup_expr='icontains')
  start_date = filters.DateFilter(field_name='last_modified', label='Start Date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))
  end_date = filters.DateFilter(field_name='last_modified', label='End Date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}))
  branch = filters.ModelChoiceFilter(queryset=Branch.objects.all(), label='Branch', lookup_expr='exact')
  stages = filters.ChoiceFilter(choices=Applicant.choice, label='Category', lookup_expr='exact')
  product = filters.ModelChoiceFilter(queryset=ProductType.objects.all(), label='Product', method='filter_by_product')

  class Meta:
    model = Applicant
    fields = {}

  def filter_by_product(self, queryset, name, value):
    return queryset.filter(user_financing_plan__app_type__product_type__financing_type=value)
