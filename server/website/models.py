from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import date

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class Pet(models.Model):
    id = models.BigAutoField(primary_key=True)
    uploadphoto1 = models.ImageField(upload_to='pets/', blank=True, null=True)
    uploadphoto2 = models.ImageField(upload_to='pets/', blank=True, null=True)
    uploadphoto3 = models.ImageField(upload_to='pets/', blank=True, null=True)
    uploadphoto4 = models.ImageField(upload_to='pets/', blank=True, null=True)
    uploadphoto5 = models.ImageField(upload_to='pets/', blank=True, null=True)

    nameOfPet = models.CharField(max_length=255, null=True)
    typeOfPet = models.CharField(max_length=255, null=True)
    petSpecies = models.CharField(max_length=255, null=True)
    petStatus= models.CharField(max_length=255, null=True)
    priceofSelling = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    dateofbirth = models.DateField(max_length=255,  default='1490-01-01')
    healthStatus = models.CharField(max_length=255, null=True)
    sickDiagnosis = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)
    AdvertiserID = models.ForeignKey(User, max_length=500, null=True, on_delete=models.CASCADE)
    
    date_added = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.nameOfPet
     
    def get_absolute_url(self):
        return f'/findpet/{self.id}/'
    
    def get_editproperty_url(self):
        return f'/editpet/{self.id}/'

    def get_age(self):
        current_year = int((date.today()).year)
        if(self.dateofbirth):
            return current_year - int(self.dateofbirth.year)
        else:
            return 0
    
    def get_uploadphoto1(self):
        if self.uploadphoto1:
            return 'http://127.0.0.1:8000' + self.uploadphoto1.url
        return ''

    def get_uploadphoto2(self):
        if self.uploadphoto2:
            return 'http://127.0.0.1:8000' + self.uploadphoto2.url
        return ''

    def get_uploadphoto3(self):
        if self.uploadphoto3:
            return 'http://127.0.0.1:8000' + self.uploadphoto3.url
        return ''

    def get_uploadphoto4(self):
        if self.uploadphoto4:
            return 'http://127.0.0.1:8000' + self.uploadphoto4.url
        return ''

    def get_uploadphoto5(self):
        if self.uploadphoto5:
            return 'http://127.0.0.1:8000' + self.uploadphoto5.url
        return ''



class UserProfile(models.Model):
    housemate_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, default='Buddy')
    username = models.CharField(max_length=255, null=True, default='buddy')
    phonenumber = models.CharField(max_length=255,  default='-')
    dateofbirth = models.DateField(max_length=255,  default='1490-01-01')
    gender = models.CharField(max_length=10,null=True, default='-')
    
    occupation = models.CharField(max_length=255,null=True, default='-')
    aboutme = models.CharField(max_length=255,null=True, default='-')
    HasPet = models.CharField(max_length=255,null=True, default='Has No Pet') #By default everyone will be registered as 'Needs A Place' until they posted a property, then this value will be changed
    petcounter = models.IntegerField(default=0)
    
    profilephoto = models.ImageField(upload_to='profilephoto/', blank=True, null=True)
    preferredcity = models.CharField(max_length=255,null=True, default='-')
    igAccount = models.CharField(max_length=255,null=True, default='-')
    fbAccount = models.CharField(max_length=255,null=True, default='-')
    

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return f'/findguardian/{self.username}/'

    def age(self):
        current_year = int((date.today()).year)
        if(self.dateofbirth):
            return current_year - int(self.dateofbirth.year)
        else:
            return 0
       
    def get_profilephoto(self):
        if self.profilephoto:
            return 'http://127.0.0.1:8000' + self.profilephoto.url
        return ''

    def get_igAccount(self):
        if self.igAccount:
            return 'https://instagram.com/' + self.igAccount
        return ''
    
    def get_fbAccount(self):
        if self.fbAccount:
            return 'https://facebook.com/' + self.fbAccount
        return ''

@receiver(post_save, sender = User) 
def create_profile(sender, instance, created, **kwargs): 
    if created:
        UserProfile.objects.get_or_create(housemate_id=instance, username=instance)
        