# Generated by Django 3.0.1 on 2021-11-02 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('music', '0003_audio_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='added_by',
        ),
        migrations.AddField(
            model_name='audio',
            name='published_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audios', to='profiles.UserProfile'),
        ),
    ]
