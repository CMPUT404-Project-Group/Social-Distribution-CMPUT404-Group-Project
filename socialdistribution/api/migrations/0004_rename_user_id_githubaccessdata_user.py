# Generated by Django 3.2.8 on 2021-11-25 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211124_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='githubaccessdata',
            old_name='user_id',
            new_name='user',
        ),
    ]
