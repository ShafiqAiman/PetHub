# Generated by Django 3.2.3 on 2022-07-14 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0057_delete_userpreferences'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='state',
            new_name='building',
        ),
    ]
