from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mykad_no = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    address_line_one = models.CharField(max_length=100, null=True, blank=True)
    address_line_two = models.CharField(max_length=100, null=True, blank=True)
    address_line_three = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    bank_account_number = models.CharField(max_length=50, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        ENTREPRENEUR = "ENTREPRENEUR", 'Entrepreneur'
        INVESTOR = "INVESTOR", 'Investor'

    role = models.CharField(max_length=50, choices=Role.choices)

    class Position(models.TextChoices):
        REVIEWER = "REVIEWER", 'Reviewer'
        CHECKER = "CHECKER", 'Checker'

    position = models.CharField(max_length=50, choices=Position.choices)

    position = models.CharField(max_length=50, choices=Position.choices, null=True, blank=True)

def __str__(self):
    return self.user.username

# Create a user Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        if not instance.is_superuser:
                UserProfile.objects.create(user=instance, role='INVESTOR')
        else:
                UserProfile.objects.create(user=instance)
    instance.userprofile.save()    

# Automate the profile thing
post_save.connect(create_profile, sender=User)