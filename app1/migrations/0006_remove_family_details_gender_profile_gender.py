# Generated by Django 4.2.4 on 2023-08-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_family_details_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family_details',
            name='gender',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
