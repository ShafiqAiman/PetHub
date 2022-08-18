# Generated by Django 3.2.3 on 2022-04-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0040_userprofile_preferredcity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='building',
            new_name='nameOfListing',
        ),
        migrations.AddField(
            model_name='house',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='typeOfRoom',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='zipcode',
            field=models.CharField(max_length=255, null=True),
        ),
    ]