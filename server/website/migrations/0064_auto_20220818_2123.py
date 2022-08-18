# Generated by Django 3.2.3 on 2022-08-18 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0063_auto_20220818_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uploadphoto1', models.ImageField(blank=True, null=True, upload_to='pets/')),
                ('uploadphoto2', models.ImageField(blank=True, null=True, upload_to='pets/')),
                ('uploadphoto3', models.ImageField(blank=True, null=True, upload_to='pets/')),
                ('uploadphoto4', models.ImageField(blank=True, null=True, upload_to='pets/')),
                ('uploadphoto5', models.ImageField(blank=True, null=True, upload_to='pets/')),
                ('nameOfPet', models.CharField(max_length=255, null=True)),
                ('typeOfPet', models.CharField(max_length=255, null=True)),
                ('petSpecies', models.CharField(max_length=255, null=True)),
                ('petStatus', models.CharField(max_length=255, null=True)),
                ('priceofSelling', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('dateofbirth', models.DateField(default='1490-01-01', max_length=255)),
                ('healthStatus', models.CharField(max_length=255, null=True)),
                ('sickDiagnosis', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('AdvertiserID', models.ForeignKey(max_length=500, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.DeleteModel(
            name='House',
        ),
    ]
