# Generated by Django 3.2.8 on 2021-12-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_merge_20211204_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='auth_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
