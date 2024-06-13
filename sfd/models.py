from django.db import models
from django.contrib.auth.admin import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_of_business = models.ForeignKey(CategoryOfBusiness, on_delete=models.CASCADE,null=True,blank=True)
    company_name = models.CharField(max_length=150, null=True,blank=True)
    company_email = models.CharField(max_length=150, null=True,blank=True)
    company_phone_number = models.CharField(max_length=150, null=True,blank=True)
    company_website = models.CharField(max_length=150, null=True,blank=True)
    company_address = models.CharField(max_length=300, null=True,blank=True)
    company_logo = models.CharField(max_length=500, default='https://i.pinimg.com/736x/72/8b/6c/728b6c0d58d7e6b29e91faf8a1a31bc4.jpg')
    company_portfolio = models.CharField(max_length=500, default='https://i.pinimg.com/736x/72/8b/6c/728b6c0d58d7e6b29e91faf8a1a31bc4.jpg')
    company_registration_number = models.CharField(max_length=150, null=True,blank=True)
    company_summary = models.CharField(max_length=300, null=True,blank=True)
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
    total_amount = models.CharField(max_length=50, null=True,blank=True)
    status = models.BooleanField(default=False)
    start_campaign = models.DateTimeField(null=True,blank=True)
    end_campaign= models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TrancheInvestor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TrancheEntreprenuer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TrancheReport(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True,blank=True)
    report = models.CharField(max_length=500, default='https://i.pinimg.com/736x/72/8b/6c/728b6c0d58d7e6b29e91faf8a1a31bc4.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


