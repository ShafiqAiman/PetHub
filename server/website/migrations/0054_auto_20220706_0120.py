# Generated by Django 3.2.3 on 2022-07-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0053_userprofile_housecounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='Page',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='Pchildren',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='Pgender',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='Poccupation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='Ppet',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='Preligion',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='Psexorientation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='Psmoking',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
