# Generated by Django 4.0.6 on 2022-07-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devind_dictionaries', '0004_auto_20220421_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetclassification',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Updated date', null=True),
        ),
    ]
