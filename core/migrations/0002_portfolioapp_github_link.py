# Generated by Django 3.2 on 2021-04-19 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioapp',
            name='github_link',
            field=models.URLField(default='github link'),
            preserve_default=False,
        ),
    ]
