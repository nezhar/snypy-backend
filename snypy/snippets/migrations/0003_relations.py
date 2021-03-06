# Generated by Django 2.0.6 on 2018-06-09 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
        ('snippets', '0002_snippet_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='user',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='snippets', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='label',
            name='snippets',
            field=models.ManyToManyField(related_name='labels', through='snippets.SnippetLabel', to='snippets.Snippet', verbose_name='Snippets'),
        ),
        migrations.AddField(
            model_name='label',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='teams.Team', verbose_name='Team'),
        ),
        migrations.AddField(
            model_name='label',
            name='user',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='labels', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='file',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='snippets.Language', verbose_name='Language'),
        ),
        migrations.AddField(
            model_name='file',
            name='snippet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='snippets.Snippet', verbose_name='Snippet'),
        ),
        migrations.AddField(
            model_name='extension',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extensions', to='snippets.Language', verbose_name='Language'),
        ),
    ]
