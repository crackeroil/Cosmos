# Generated by Django 3.0.8 on 2020-09-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms_plugins", "0002_initial_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="committeelistpluginmodel",
            name="button",
            field=models.BooleanField(default=True, verbose_name="use button"),
        ),
    ]
