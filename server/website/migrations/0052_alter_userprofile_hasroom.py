# Generated by Django 3.2.3 on 2022-06-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0051_auto_20220530_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='HasRoom',
            field=models.CharField(default='Needs A Place', max_length=255, null=True),
        ),
    ]
