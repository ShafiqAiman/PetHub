# Generated by Django 3.2.3 on 2022-01-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_alter_userprofile_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dateofbirth',
            field=models.DateField(default='1490-01-01', max_length=255),
        ),
    ]