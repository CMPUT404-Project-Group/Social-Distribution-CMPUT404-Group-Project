# Generated by Django 3.2.8 on 2021-10-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_like_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='object_id',
            field=models.CharField(max_length=255),
        ),
    ]
