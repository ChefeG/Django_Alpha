# Generated by Django 3.2.6 on 2021-09-01 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210901_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='districts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.districts', verbose_name='район'),
        ),
    ]
