# Generated by Django 3.2.6 on 2021-08-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_districtsnews_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='districts',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Черновик'),
        ),
    ]
