# Generated by Django 4.2.4 on 2023-08-10 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_city_qualification_work'),
    ]

    operations = [
        migrations.DeleteModel(
            name='city',
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
        migrations.DeleteModel(
            name='work',
        ),
    ]