from django.db import models
from .helper import check_file_type
from users.models import UserProfile


# Validate File
def validate_file_image(value):
	if not check_file_type(value, ['pdf']):
		raise ValidationError(
			('%(value)s is not a valid file.'),
			params={'value': value},
		)

def validate_file_document(value):
	if not check_file_type(value, ['png', 'jpg']):
		raise ValidationError(
			('%(value)s is not a valid file.'),
			params={'value': value},
		)

# Create your models here.
class NatureOfBusiness(models.Model):
	title = models.CharField(max_length=150, null=True,blank=True)
	description = models.CharField(max_length=150, null=True,blank=True)
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
    
class CategoryOfBusiness(models.Model):
	nature_of_business = models.ForeignKey(NatureOfBusiness, on_delete=models.CASCADE, null=True,blank=True)
	title = models.CharField(max_length=150, null=True,blank=True)
	description = models.CharField(max_length=150, null=True,blank=True)
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class CompanyProfile(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name="user_company")
	category_of_business = models.ForeignKey(CategoryOfBusiness, on_delete=models.CASCADE,null=True,blank=True)
	company_name = models.CharField(max_length=150, null=True,blank=True)
	company_email = models.CharField(max_length=150, null=True,blank=True)
	company_phone_number = models.CharField(max_length=150, null=True,blank=True)
	company_website = models.CharField(max_length=150, null=True,blank=True)
	company_address = models.CharField(max_length=300, null=True,blank=True)
	company_logo = models.FileField(upload_to='company/logo/', verbose_name='Company Logo', blank=True, null=True, validators=[validate_file_image], help_text='Format Image is PNG and JPG only')
	company_portfolio = models.FileField(upload_to='company/portfolio/', verbose_name='Company Portfolio', blank=True, null=True, validators=[validate_file_image], help_text='Format Image is PNG and JPG only')
	company_registration_number = models.CharField(max_length=150, null=True,blank=True)
	company_summary = models.CharField(max_length=1000, null=True,blank=True)
	financing_amount = models.CharField(max_length=100, null=True,blank=True)
	grant_amount = models.CharField(max_length=100, null=True,blank=True)
	company_status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.company_name

class Campaign(models.Model):
	title = models.CharField(max_length=150, null=True,blank=True)
	description = models.CharField(max_length=150, null=True,blank=True)
	campaign_summary = models.CharField(max_length=300, null=True,blank=True)
	campaign_logo = models.FileField(upload_to='campaign/logo/', verbose_name="Campaign Logo", blank=True, null=True, validators=[validate_file_image], help_text="Format Image is PNG and JPG only")
	total_amount = models.CharField(max_length=50, null=True,blank=True)
	min_target_amount = models.CharField(max_length=50, null=True,blank=True)
	status = models.BooleanField(default=False)
	start_campaign = models.DateTimeField(null=True,blank=True)
	end_campaign= models.DateTimeField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class TrancheInvestor(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True,blank=True)
	campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
	invest_amount = models.CharField(max_length=50, null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user
    

class TrancheEntrepreneur(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True,blank=True)
	campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user

class TrancheReport(models.Model):
	campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True,blank=True)
	quarter = models.CharField(max_length=200, null=True,blank=True)
	filename = models.CharField(max_length=300, null=True,blank=True)
	report = models.CharField(max_length=500, null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user

