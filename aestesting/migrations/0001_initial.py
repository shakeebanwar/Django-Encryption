# Generated by Django 3.1.3 on 2020-11-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health_Professional_Account',
            fields=[
                ('Health_Professional_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Full_Name', models.CharField(default='', max_length=100)),
                ('First_Name', models.CharField(default='', max_length=100)),
                ('Last_Name', models.CharField(default='', max_length=100)),
                ('Email', models.EmailField(default='', max_length=100)),
                ('Username', models.CharField(default='', max_length=100)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('Date_of_Birth', models.CharField(default='', max_length=200)),
                ('Password', models.CharField(default='', max_length=3000)),
                ('Degree', models.CharField(default='', max_length=200)),
                ('Affiliation', models.CharField(default='', max_length=200)),
                ('Bio', models.TextField(default='')),
                ('Street_Address', models.CharField(default='', max_length=500)),
                ('City', models.CharField(default='', max_length=500)),
                ('State', models.CharField(default='', max_length=500)),
                ('Country', models.CharField(default='', max_length=500)),
                ('Location', models.CharField(default='', max_length=500)),
                ('Role', models.CharField(default='earhealthprofessional', max_length=100)),
                ('Status', models.CharField(choices=[('Available', 'Available'), ('Not_Available', 'Not_Available')], default='Available', max_length=100)),
                ('Mobile_Number', models.CharField(default='', max_length=200)),
                ('Email_Verification_Code', models.CharField(default='', max_length=200)),
                ('OTP_Verification', models.CharField(default='12345', max_length=200)),
                ('Doctor_rating', models.IntegerField(default=0)),
                ('Doctor_rating_Count', models.IntegerField(default=0)),
            ],
        ),
    ]
