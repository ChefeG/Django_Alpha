# Generated by Django 3.2.6 on 2021-08-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
    ]