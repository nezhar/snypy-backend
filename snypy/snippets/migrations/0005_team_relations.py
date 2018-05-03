# Generated by Django 2.0.5 on 2018-05-03 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('snippets', '0004_fix_related_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='teams.Team', verbose_name='Team'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='teams.Team', verbose_name='Team'),
        ),
    ]
