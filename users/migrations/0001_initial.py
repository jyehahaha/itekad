# Generated by Django 4.2.4 on 2024-06-11 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mykad_no', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_three', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('ENTREPRENEUR', 'Entrepreneur'), ('INVESTOR', 'Investor')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mykad_no', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_three', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('ENTREPRENEUR', 'Entrepreneur'), ('INVESTOR', 'Investor')], max_length=50, null=True)),
                ('position', models.CharField(blank=True, choices=[('REVIEWER', 'Reviewer'), ('CHECKER', 'Checker')], max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mykad_no', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_three', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('ENTREPRENEUR', 'Entrepreneur'), ('INVESTOR', 'Investor')], max_length=50, null=True)),
                ('position', models.CharField(blank=True, choices=[('REVIEWER', 'Reviewer'), ('CHECKER', 'Checker')], max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mykad_no', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line_three', models.CharField(blank=True, max_length=100, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('ENTREPRENEUR', 'Entrepreneur'), ('INVESTOR', 'Investor')], max_length=50, null=True)),
                ('position', models.CharField(blank=True, choices=[('REVIEWER', 'Reviewer'), ('CHECKER', 'Checker')], max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
