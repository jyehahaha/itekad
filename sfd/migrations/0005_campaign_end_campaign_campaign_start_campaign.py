# Generated by Django 4.2.4 on 2024-06-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfd', '0004_campaign_description_alter_trancheentreprenuer_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='end_campaign',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='start_campaign',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]