# Generated by Django 3.2.3 on 2021-06-07 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_userprofile_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='thumbnail',
            new_name='profilethumbnail',
        ),
    ]