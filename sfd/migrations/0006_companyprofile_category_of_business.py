# Generated by Django 4.2.4 on 2024-06-12 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sfd', '0005_campaign_end_campaign_campaign_start_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='category_of_business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sfd.categoryofbusiness'),
        ),
    ]