# Generated by Django 3.2.6 on 2021-08-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_districtsimage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtsimage',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
