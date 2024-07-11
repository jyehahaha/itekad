from django import forms
from django.forms import (
  ModelForm,
  DateTimeInput,
)
from sfd.models import (
  CompanyProfile,
  Campaign,
  TrancheEntrepreneur,
  TrancheInvestor,
  TrancheReport,
  NatureOfBusiness,
  CategoryOfBusiness,
)

# Create your forms here.
class DateTimeInputCustom(DateTimeInput):
  input_type = 'date'

class CompanyProfileForm(ModelForm):
  class Meta:
    model = CompanyProfile
    # fields = ["company_name","company_email","company_phone_number","company_website","company_address","company_logo","company_portfolio","company_registration_number","company_summary","financing_amount","grant_amount","company_status"]
    fields = "__all__"
    widgets = {
      'company_summary': forms.Textarea()
    }
    labels = {
      'company_email': "E-mail Address",
      'company_website': "Website",
      'company_address': "Address",
      'company_logo': "Logo",
      'company_registration_number': "Company SSM Number",
      'company_summary': "Company Summary Background",
      'financing_amount': 'Financing Amount(RM)',
      'grant_amount': 'Grant Amount(RM)',
      'company_status': "Status"
    }

class CampaignForm(ModelForm):
  class Meta:
    model = Campaign
    fields = "__all__"
    widgets = {
      'campaign_summary': forms.Textarea(),
      'start_campaign': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type':'datetime-local'}),
      'end_campaign': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type':'datetime-local'}),
    }

class TrancheEntrepreneurForm(ModelForm):
  class Meta:
    model = TrancheEntrepreneur
    fields = "__all__"

class TrancheInvestorForm(ModelForm):
  class Meta:
    model = TrancheInvestor
    fields = "__all__"
    labels = {
      'user': 'Investor',
      'campaign': 'Campaign',
      'invest_amount': 'Investment Amount (RM)',
    }

class TrancheReportForm(ModelForm):
  class Meta:
    model = TrancheReport
    fields = "__all__"

class NatureOfBusinessForm(ModelForm):
  class Meta:
    model = NatureOfBusiness
    fields = "__all__"
    widgets = {
      'description': forms.Textarea()
    }

class CategoryOfBusinessForm(ModelForm):
  class Meta:
    model = CategoryOfBusiness
    fields = "__all__"
    widgets = {
      'description': forms.Textarea()
    }