# Generated by Django 3.2.13 on 2022-04-20 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devind_dictionaries', '0002_auto_20220407_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Code', max_length=40, unique=True)),
                ('name', models.CharField(help_text='Name', max_length=1024)),
                ('active', models.BooleanField(default=True, help_text='Active')),
                ('start', models.DateTimeField(auto_now_add=True, help_text='Date of start activity')),
                ('end', models.DateTimeField(help_text='Date of end activity', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated date')),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.IntegerField(default=None, help_text='Code of department', null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='minister',
            field=models.ForeignKey(help_text='Responsible Minister', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='minister', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(help_text='Department name', max_length=255),
        ),
        migrations.AlterField(
            model_name='department',
            name='organizations',
            field=models.ManyToManyField(help_text='Related organizations', to='devind_dictionaries.Organization'),
        ),
        migrations.AlterField(
            model_name='department',
            name='user',
            field=models.ForeignKey(help_text='Director of department', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department',
            name='users',
            field=models.ManyToManyField(help_text='Users in departments', related_name='departments', to=settings.AUTH_USER_MODEL),
        ),
    ]
