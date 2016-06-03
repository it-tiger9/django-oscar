# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 20:48
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models
import wellsfargo.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oscar_accounts', '0003_alter_ip_address'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountMetadata',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='wfrs_metadata', serialize=False, to='oscar_accounts.Account', verbose_name='Account')),  # NOQA
                ('locale', models.CharField(choices=[('en_US', 'English (US)'), ('en_CA', 'English (CA)'), ('fr_CA', 'French (CA)')], max_length=5, verbose_name='Locale')),  # NOQA
                ('account_number', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16), django.core.validators.MinLengthValidator(16)], verbose_name='Wells Fargo Account Number')),  # NOQA
            ],
        ),
        migrations.CreateModel(
            name='CACreditApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('US', 'United States'), ('CA', 'Canada')], max_length=15, verbose_name='Region')),
                ('language', models.CharField(choices=[('E', 'English'), ('F', 'French')], max_length=1, verbose_name='Language')),
                ('app_type', models.CharField(choices=[('I', 'Individual'), ('J', 'Joint')], max_length=1, verbose_name='Application Type')),
                ('purchase_price', models.IntegerField(blank=True, null=True, verbose_name='Requested Credit Amount')),
                ('main_first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('main_last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('main_middle_initial', models.CharField(blank=True, max_length=1, null=True, verbose_name='Middle Initial')),
                ('main_date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('main_address_line1', models.CharField(max_length=35, verbose_name='Address Line 1')),
                ('main_address_line2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address Line 2')),
                ('main_address_city', models.CharField(max_length=15, verbose_name='City')),
                ('main_home_value', models.IntegerField(blank=True, null=True, verbose_name='Home Value')),
                ('main_mortgage_balance', models.IntegerField(blank=True, null=True, verbose_name='Mortgage Balance')),
                ('main_annual_income', models.IntegerField(verbose_name='Annual Income')),
                ('insurance', models.BooleanField(verbose_name='Optional Insurance')),
                ('sales_person_id', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Existing Sales Person ID')),  # NOQA
                ('new_sales_person', models.CharField(blank=True, max_length=10, null=True, verbose_name='New Sales Person Name')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('main_ssn', wellsfargo.core.fields.CASocialInsuranceNumberField(blank=True, null=True, verbose_name='Social Insurance Number')),
                ('main_address_state', wellsfargo.core.fields.CAProvinceField(verbose_name='Province')),
                ('main_address_postcode', wellsfargo.core.fields.CAPostalCodeField(verbose_name='Postcode')),
                ('main_home_phone', wellsfargo.core.fields.CAPhoneNumberField(verbose_name='Home Phone')),
                ('main_time_at_address', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Address')),  # NOQA
                ('main_housing_status', models.CharField(choices=[('R', 'Rent'), ('O', 'Own')], max_length=3, verbose_name='Housing Status')),
                ('main_employer_name', models.CharField(max_length=30, verbose_name='Employer Name')),
                ('main_time_at_employer', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Employer')),  # NOQA
                ('main_employer_phone', wellsfargo.core.fields.CAPhoneNumberField(verbose_name='Employer Phone Number')),
                ('main_cell_phone', wellsfargo.core.fields.CAPhoneNumberField(blank=True, null=True, verbose_name='Cell Phone')),
                ('main_occupation', models.CharField(max_length=24, verbose_name='Occupation')),
                ('main_photo_id_type', models.CharField(choices=[('OA', 'Old Age Security Card'), ('DL', 'Driver’s License'), ('PI', 'Provincial ID'), ('PA', 'Canadian Passport'), ('CN', 'Certificate of Citizenship or Naturalization'), ('IS', 'Certificate of Indian Status'), ('CC', 'Canadian Citizen Form 1000 or 1442')], max_length=2, verbose_name='Photo ID Type')),  # NOQA
                ('main_photo_id_number', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Photo ID Number')),  # NOQA
                ('main_drivers_license_province', wellsfargo.core.fields.CAProvinceField(blank=True, null=True, verbose_name='Driver’s License Province')),
                ('main_photo_id_expiration', models.DateField(verbose_name='Photo ID Expiration Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CAJointCreditApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('US', 'United States'), ('CA', 'Canada')], max_length=15, verbose_name='Region')),
                ('language', models.CharField(choices=[('E', 'English'), ('F', 'French')], max_length=1, verbose_name='Language')),
                ('app_type', models.CharField(choices=[('I', 'Individual'), ('J', 'Joint')], max_length=1, verbose_name='Application Type')),
                ('purchase_price', models.IntegerField(blank=True, null=True, verbose_name='Requested Credit Amount')),
                ('main_first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('main_last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('main_middle_initial', models.CharField(blank=True, max_length=1, null=True, verbose_name='Middle Initial')),
                ('main_date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('main_address_line1', models.CharField(max_length=35, verbose_name='Address Line 1')),
                ('main_address_line2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address Line 2')),
                ('main_address_city', models.CharField(max_length=15, verbose_name='City')),
                ('main_home_value', models.IntegerField(blank=True, null=True, verbose_name='Home Value')),
                ('main_mortgage_balance', models.IntegerField(blank=True, null=True, verbose_name='Mortgage Balance')),
                ('main_annual_income', models.IntegerField(verbose_name='Annual Income')),
                ('insurance', models.BooleanField(verbose_name='Optional Insurance')),
                ('sales_person_id', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Existing Sales Person ID')),  # NOQA
                ('new_sales_person', models.CharField(blank=True, max_length=10, null=True, verbose_name='New Sales Person Name')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('joint_first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('joint_last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('joint_middle_initial', models.CharField(blank=True, max_length=1, null=True, verbose_name='Middle Initial')),
                ('joint_date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('joint_address_line1', models.CharField(max_length=35, verbose_name='Address Line 1')),
                ('joint_address_line2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address Line 2')),
                ('joint_address_city', models.CharField(max_length=15, verbose_name='City')),
                ('joint_annual_income', models.IntegerField(verbose_name='Annual Income')),
                ('main_ssn', wellsfargo.core.fields.CASocialInsuranceNumberField(blank=True, null=True, verbose_name='Social Insurance Number')),
                ('main_address_state', wellsfargo.core.fields.CAProvinceField(verbose_name='Province')),
                ('main_address_postcode', wellsfargo.core.fields.CAPostalCodeField(verbose_name='Postcode')),
                ('main_home_phone', wellsfargo.core.fields.CAPhoneNumberField(verbose_name='Home Phone')),
                ('main_time_at_address', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Address')),  # NOQA
                ('main_housing_status', models.CharField(choices=[('R', 'Rent'), ('O', 'Own')], max_length=3, verbose_name='Housing Status')),
                ('main_employer_name', models.CharField(max_length=30, verbose_name='Employer Name')),
                ('main_time_at_employer', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Employer')),  # NOQA
                ('main_employer_phone', wellsfargo.core.fields.CAPhoneNumberField(verbose_name='Employer Phone Number')),
                ('main_cell_phone', wellsfargo.core.fields.CAPhoneNumberField(blank=True, null=True, verbose_name='Cell Phone')),
                ('main_occupation', models.CharField(max_length=24, verbose_name='Occupation')),
                ('main_photo_id_type', models.CharField(choices=[('OA', 'Old Age Security Card'), ('DL', 'Driver’s License'), ('PI', 'Provincial ID'), ('PA', 'Canadian Passport'), ('CN', 'Certificate of Citizenship or Naturalization'), ('IS', 'Certificate of Indian Status'), ('CC', 'Canadian Citizen Form 1000 or 1442')], max_length=2, verbose_name='Photo ID Type')),  # NOQA
                ('main_photo_id_number', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Photo ID Number')),  # NOQA
                ('main_drivers_license_province', wellsfargo.core.fields.CAProvinceField(blank=True, null=True, verbose_name='Driver’s License Province')),
                ('main_photo_id_expiration', models.DateField(verbose_name='Photo ID Expiration Date')),
                ('joint_ssn', wellsfargo.core.fields.CASocialInsuranceNumberField(blank=True, null=True, verbose_name='Social Insurance Number')),
                ('joint_address_state', wellsfargo.core.fields.CAProvinceField(verbose_name='Province')),
                ('joint_address_postcode', wellsfargo.core.fields.CAPostalCodeField(verbose_name='Postcode')),
                ('joint_employer_name', models.CharField(max_length=30, verbose_name='Employer Name')),
                ('joint_time_at_employer', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Employer')),  # NOQA
                ('joint_employer_phone', wellsfargo.core.fields.CAPhoneNumberField(verbose_name='Employer Phone Number')),
                ('joint_cell_phone', wellsfargo.core.fields.CAPhoneNumberField(blank=True, null=True, verbose_name='Cell Phone')),
                ('joint_occupation', models.CharField(max_length=24, verbose_name='Occupation')),
                ('joint_photo_id_type', models.CharField(choices=[('OA', 'Old Age Security Card'), ('DL', 'Driver’s License'), ('PI', 'Provincial ID'), ('PA', 'Canadian Passport'), ('CN', 'Certificate of Citizenship or Naturalization'), ('IS', 'Certificate of Indian Status'), ('CC', 'Canadian Citizen Form 1000 or 1442')], max_length=3, verbose_name='Photo ID Type')),  # NOQA
                ('joint_photo_id_number', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Photo ID Number')),  # NOQA
                ('joint_drivers_license_province', wellsfargo.core.fields.CAProvinceField(blank=True, null=True, verbose_name='Driver’s License Province')),
                ('joint_photo_id_expiration', models.DateField(verbose_name='Photo ID Expiration Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_code', models.CharField(choices=[('5', 'Authorization for Future Charge'), ('7', 'Cancel Existing Authorization'), ('4', 'Return or Credit'), ('9', 'Time-out Reversal for Return or Credit'), ('VS', 'Void Sale'), ('VR', 'Void Return')], default='5', max_length=2, verbose_name='Transaction Type')),  # NOQA
                ('ticket_number', models.CharField(blank=True, max_length=12, null=True, verbose_name='Ticket Number')),
                ('plan_number', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Plan Number')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('auth_number', models.CharField(default='000000', max_length=6, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MinLengthValidator(6), django.core.validators.RegexValidator('^[0-9]{6}$')], verbose_name='Authorization Number')),  # NOQA
                ('dest_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest_requests', to='oscar_accounts.Account', verbose_name='Destination Account')),  # NOQA
                ('source_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_requests', to='oscar_accounts.Account', verbose_name='Source Account')),  # NOQA
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_requests', to=settings.AUTH_USER_MODEL, verbose_name='Requesting User')),  # NOQA
            ],
        ),
        migrations.CreateModel(
            name='TransferMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_code', models.CharField(choices=[('5', 'Authorization for Future Charge'), ('7', 'Cancel Existing Authorization'), ('4', 'Return or Credit'), ('9', 'Time-out Reversal for Return or Credit'), ('VS', 'Void Sale'), ('VR', 'Void Return')], max_length=2, verbose_name='Transaction Type')),  # NOQA
                ('ticket_number', models.CharField(blank=True, max_length=12, null=True, verbose_name='Ticket Number')),
                ('plan_number', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MinValueValidator(1001), django.core.validators.MaxValueValidator(9999)], verbose_name='Plan Number')),  # NOQA
                ('auth_number', models.CharField(blank=True, default='000000', max_length=6, null=True, verbose_name='Authorization Number')),
                ('status', models.CharField(choices=[('A0', 'Transaction not approved or declined. For time-out reversal and void transactions, match was found but was already funded.'), ('A1', 'Approved. For time-out reversal and void transactions, match was found and processed.'), ('A2', 'Time-out reversal or void approved, but no matching transaction was found.'), ('A3', 'Time-out reversal or void approved, but matched duplicate transactions.')], max_length=2, verbose_name='Status')),  # NOQA
                ('message', models.TextField(verbose_name='Message')),
                ('disclosure', models.TextField(verbose_name='Disclosure')),
                ('transfer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wfrs_metadata', to='oscar_accounts.Transfer', verbose_name='Transfer')),  # NOQA
            ],
        ),
        migrations.CreateModel(
            name='USCreditApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('US', 'United States'), ('CA', 'Canada')], max_length=15, verbose_name='Region')),
                ('language', models.CharField(choices=[('E', 'English'), ('F', 'French')], max_length=1, verbose_name='Language')),
                ('app_type', models.CharField(choices=[('I', 'Individual'), ('J', 'Joint')], max_length=1, verbose_name='Application Type')),
                ('purchase_price', models.IntegerField(blank=True, null=True, verbose_name='Requested Credit Amount')),
                ('main_first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('main_last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('main_middle_initial', models.CharField(blank=True, max_length=1, null=True, verbose_name='Middle Initial')),
                ('main_date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('main_address_line1', models.CharField(max_length=35, verbose_name='Address Line 1')),
                ('main_address_line2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address Line 2')),
                ('main_address_city', models.CharField(max_length=15, verbose_name='City')),
                ('main_home_value', models.IntegerField(blank=True, null=True, verbose_name='Home Value')),
                ('main_mortgage_balance', models.IntegerField(blank=True, null=True, verbose_name='Mortgage Balance')),
                ('main_annual_income', models.IntegerField(verbose_name='Annual Income')),
                ('insurance', models.BooleanField(verbose_name='Optional Insurance')),
                ('sales_person_id', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Existing Sales Person ID')),  # NOQA
                ('new_sales_person', models.CharField(blank=True, max_length=10, null=True, verbose_name='New Sales Person Name')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('main_ssn', wellsfargo.core.fields.USSocialSecurityNumberField(verbose_name='Social Security Number')),
                ('main_address_state', localflavor.us.models.USStateField(verbose_name='State')),
                ('main_address_postcode', localflavor.us.models.USZipCodeField(verbose_name='Postcode')),
                ('main_home_phone', localflavor.us.models.PhoneNumberField(verbose_name='Home Phone')),
                ('main_time_at_address', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Address')),  # NOQA
                ('main_housing_status', models.CharField(blank=True, choices=[('R', 'Rent'), ('O', 'Own'), ('OT', 'Other')], max_length=3, null=True, verbose_name='Housing Status')),  # NOQA
                ('main_employer_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Employer Name')),
                ('main_time_at_employer', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Employer')),  # NOQA
                ('main_employer_phone', localflavor.us.models.PhoneNumberField(verbose_name='Employer Phone Number')),
                ('main_cell_phone', localflavor.us.models.PhoneNumberField(blank=True, null=True, verbose_name='Cell Phone')),
                ('main_occupation', models.CharField(blank=True, max_length=24, null=True, verbose_name='Occupation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USJointCreditApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('US', 'United States'), ('CA', 'Canada')], max_length=15, verbose_name='Region')),
                ('language', models.CharField(choices=[('E', 'English'), ('F', 'French')], max_length=1, verbose_name='Language')),
                ('app_type', models.CharField(choices=[('I', 'Individual'), ('J', 'Joint')], max_length=1, verbose_name='Application Type')),
                ('purchase_price', models.IntegerField(blank=True, null=True, verbose_name='Requested Credit Amount')),
                ('main_first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('main_last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('main_middle_initial', models.CharField(blank=True, max_length=1, null=True, verbose_name='Middle Initial')),
                ('main_date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('main_address_line1', models.CharField(max_length=35, verbose_name='Address Line 1')),
                ('main_address_line2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address Line 2')),
                ('main_address_city', models.CharField(max_length=15, verbose_name='City')),
                ('main_home_value', models.IntegerField(blank=True, null=True, verbose_name='Home Value')),
                ('main_mortgage_balance', models.IntegerField(blank=True, null=True, verbose_name='Mortgage Balance')),
                ('main_annual_income', models.IntegerField(verbose_name='Annual Income')),
                ('insurance', models.BooleanField(verbose_name='Optional Insurance')),
                ('sales_person_id', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Existing Sales Person ID')),  # NOQA
                ('new_sales_person', models.CharField(blank=True, max_length=10, null=True, verbose_name='New Sales Person Name')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('joint_first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('joint_last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('joint_middle_initial', models.CharField(blank=True, max_length=1, null=True, verbose_name='Middle Initial')),
                ('joint_date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('joint_address_line1', models.CharField(max_length=35, verbose_name='Address Line 1')),
                ('joint_address_line2', models.CharField(blank=True, max_length=35, null=True, verbose_name='Address Line 2')),
                ('joint_address_city', models.CharField(max_length=15, verbose_name='City')),
                ('joint_annual_income', models.IntegerField(verbose_name='Annual Income')),
                ('main_ssn', wellsfargo.core.fields.USSocialSecurityNumberField(verbose_name='Social Security Number')),
                ('main_address_state', localflavor.us.models.USStateField(verbose_name='State')),
                ('main_address_postcode', localflavor.us.models.USZipCodeField(verbose_name='Postcode')),
                ('main_home_phone', localflavor.us.models.PhoneNumberField(verbose_name='Home Phone')),
                ('main_time_at_address', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Address')),  # NOQA
                ('main_housing_status', models.CharField(blank=True, choices=[('R', 'Rent'), ('O', 'Own'), ('OT', 'Other')], max_length=3, null=True, verbose_name='Housing Status')),  # NOQA
                ('main_employer_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Employer Name')),
                ('main_time_at_employer', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Employer')),  # NOQA
                ('main_employer_phone', localflavor.us.models.PhoneNumberField(verbose_name='Employer Phone Number')),
                ('main_cell_phone', localflavor.us.models.PhoneNumberField(blank=True, null=True, verbose_name='Cell Phone')),
                ('main_occupation', models.CharField(blank=True, max_length=24, null=True, verbose_name='Occupation')),
                ('joint_ssn', wellsfargo.core.fields.USSocialSecurityNumberField(verbose_name='Social Security Number')),
                ('joint_address_state', localflavor.us.models.USStateField(verbose_name='State')),
                ('joint_address_postcode', localflavor.us.models.USZipCodeField(verbose_name='Postcode')),
                ('joint_employer_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Employer Name')),
                ('joint_time_at_employer', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4), django.core.validators.RegexValidator('^[0-9]{4}$')], verbose_name='Time at Employer')),  # NOQA
                ('joint_employer_phone', localflavor.us.models.PhoneNumberField(verbose_name='Employer Phone Number')),
                ('joint_cell_phone', localflavor.us.models.PhoneNumberField(blank=True, null=True, verbose_name='Cell Phone')),
                ('joint_occupation', models.CharField(blank=True, max_length=24, null=True, verbose_name='Occupation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
