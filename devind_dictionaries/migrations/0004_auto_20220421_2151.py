# Generated by Django 3.2.13 on 2022-04-21 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devind_dictionaries', '0003_auto_20220420_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='user',
            field=models.ForeignKey(help_text='Director of organization', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(help_text='Users in organization', related_name='organizations', to=settings.AUTH_USER_MODEL),
        ),
    ]