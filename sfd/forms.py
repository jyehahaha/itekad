from django.forms import ModelForm
from sfd.models import CompanyProfile,Campaign,TrancheEntreprenuer,TrancheInvestor,TrancheReport,NatureOfBusiness,CategoryOfBusiness
from django import forms

class CompanyProfileForm(ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ["company_name","company_email","company_phone_number","company_website","company_address","company_logo","company_portfolio","company_registration_number","company_summary","financing_amount","grant_amount","company_status"]

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ["title","status","total_amount"]

class TrancheEntreprenuerForm(ModelForm):
    class Meta:
        model = TrancheEntreprenuer
        fields = "__all__"

class TrancheInvestorForm(ModelForm):
    class Meta:
        model = TrancheInvestor
        fields = "__all__"

class TrancheReportForm(ModelForm):
    class Meta:
        model = TrancheReport
        fields = "__all__"

class NatureOfBusinessForm(ModelForm):
    class Meta:
        model = NatureOfBusiness
        fields = ["title","description","category_of_business","status"]
        widgets = {
            'description': forms.Textarea()
        }

class CategoryOfBusinessForm(ModelForm):
    class Meta:
        model = CategoryOfBusiness
        fields = ["title","description","status"]
        widgets = {
            'description': forms.Textarea()
        }