# Generated by Django 3.2.6 on 2021-08-31 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_reviews_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districts',
            name='url',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='districtsimage',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
