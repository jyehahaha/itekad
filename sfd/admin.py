from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CategoryOfBusiness)
admin.site.register(models.NatureOfBusiness)
admin.site.register(models.Campaign)
admin.site.register(models.CompanyProfile)
admin.site.register(models.TrancheInvestor)
admin.site.register(models.TrancheEntrepreneur)
admin.site.register(models.TrancheReport)