# Generated by Django 3.2.8 on 2021-10-26 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_post_shared_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shared_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.post'),
        ),
    ]