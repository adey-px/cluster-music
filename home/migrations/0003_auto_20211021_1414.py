# Generated by Django 3.0.1 on 2021-10-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211021_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='label',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
