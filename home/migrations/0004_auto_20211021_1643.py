# Generated by Django 3.0.1 on 2021-10-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211021_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='label',
            field=models.ImageField(upload_to=''),
        ),
    ]
