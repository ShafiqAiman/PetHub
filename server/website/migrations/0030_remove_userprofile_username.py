# Generated by Django 3.2.3 on 2021-12-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_alter_userprofile_housemate_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]
