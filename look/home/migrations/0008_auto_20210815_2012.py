# Generated by Django 3.2.6 on 2021-08-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210815_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='districts',
            name='apart_image',
            field=models.ImageField(null=True, upload_to='districts_apart/'),
        ),
        migrations.AddField(
            model_name='districts',
            name='apart_price',
            field=models.CharField(max_length=50, null=True),
        ),
    ]