# Generated by Django 3.2.3 on 2022-07-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0052_alter_userprofile_hasroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='housecounter',
            field=models.IntegerField(default=0),
        ),
    ]
