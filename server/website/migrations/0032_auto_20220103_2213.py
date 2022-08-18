# Generated by Django 3.2.3 on 2022-01-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dateofbirth',
            field=models.DateField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fullname',
            field=models.CharField(default='Buddy', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='orientation',
            field=models.CharField(default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pet',
            field=models.CharField(default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phonenumber',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='religion',
            field=models.CharField(default='-', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='buddy', max_length=255, null=True),
        ),
    ]