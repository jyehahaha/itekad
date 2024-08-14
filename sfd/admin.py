from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.NatureOfBusiness)
admin.site.register(models.Campaign)
admin.site.register(models.CompanyProfile)
admin.site.register(models.TrancheInvestor)
admin.site.register(models.TrancheEntrepreneur)
admin.site.register(models.TrancheReport)
admin.site.register(models.GalleryEntrepreneur)

@admin.register(models.CategoryOfBusiness)
class CategoryOfBusinessAdmin(admin.ModelAdmin):
  list_select_related = ['nature_of_business']
