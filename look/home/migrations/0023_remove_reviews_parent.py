# Generated by Django 3.2.6 on 2021-08-31 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_reviews_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='parent',
        ),
    ]
