# Generated by Django 3.2.3 on 2022-03-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_auto_20220331_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='preferredcity',
            field=models.CharField(default='-', max_length=255, null=True),
        ),
    ]
