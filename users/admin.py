from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)


# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False

# class AccountsUserAdmin(AuthUserAdmin):
#     def add_view(self, *args, **kwargs):
#         self.inlines =[]
#         return super(AccountsUserAdmin, self).add_view(*args, **kwargs)

#     def change_view(self, *args, **kwargs):
#         self.inlines =[UserProfileInline]
#         return super(AccountsUserAdmin, self).change_view(*args, **kwargs)


