# Generated by Django 2.2.20 on 2021-12-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='tool_url',
            field=models.CharField(max_length=2083),
        ),
    ]
