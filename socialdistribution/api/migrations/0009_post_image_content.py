# Generated by Django 3.2.8 on 2021-10-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_post_image_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_content',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]