# Generated by Django 3.2.8 on 2021-11-29 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20211125_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='user',
            field=models.ForeignKey(default='bbdfdd83ab144c3db54b464259bea97f', on_delete=django.db.models.deletion.CASCADE, to='api.user'),
            preserve_default=False,
        ),
    ]