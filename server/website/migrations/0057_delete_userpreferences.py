# Generated by Django 3.2.3 on 2022-07-06 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0056_alter_house_typeofroom'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPreferences',
        ),
    ]
