from django.contrib import admin
from .models import CategoryOfBusiness, NatureOfBusiness,Campaign,CompanyProfile


# Register your models here.
admin.site.register(CategoryOfBusiness)

admin.site.register(NatureOfBusiness)

admin.site.register(Campaign)

admin.site.register(CompanyProfile)




