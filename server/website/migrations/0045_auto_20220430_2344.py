# Generated by Django 3.2.3 on 2022-04-30 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0044_auto_20220406_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpreferences',
            old_name='preferredChildrenStatus',
            new_name='PGender',
        ),
        migrations.RenameField(
            model_name='userpreferences',
            old_name='preferredAge',
            new_name='Page',
        ),
        migrations.RenameField(
            model_name='userpreferences',
            old_name='preferredGender',
            new_name='Pchildren',
        ),
        migrations.RenameField(
            model_name='userpreferences',
            old_name='preferredOccupation',
            new_name='Poccupation',
        ),
        migrations.RenameField(
            model_name='userpreferences',
            old_name='preferredOrientation',
            new_name='Ppet',
        ),
        migrations.RenameField(
            model_name='userpreferences',
            old_name='preferredReligion',
            new_name='Preligion',
        ),
        migrations.RenameField(
            model_name='userpreferences',
            old_name='preferredPetStatus',
            new_name='Psexorientation',
        ),
        migrations.RenameField(
            model_name='userpreferences',
            old_name='preferredSmokingStatus',
            new_name='Psmoking',
        ),
    ]
