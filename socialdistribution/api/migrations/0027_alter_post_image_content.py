# Generated by Django 3.2.8 on 2021-12-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_node_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_content',
            field=models.ImageField(blank=True, max_length=60000, upload_to='images/'),
        ),
    ]
