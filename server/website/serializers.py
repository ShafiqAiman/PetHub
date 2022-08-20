from django.db.models import fields
from rest_framework import serializers

from .models import Pet, UserProfile

class PetSerializer(serializers.
ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            "id",
            "get_absolute_url",
            "get_editproperty_url",

            "nameOfPet",
            "typeOfPet",
            "petSpecies",
            "petStatus",
            "priceofSelling",
            "dateofbirth",
            "healthStatus",
            "sickDiagnosis",
            "description",
            "AdvertiserID",
            "get_age",
            "uploadphoto1",
            "uploadphoto2",
            "uploadphoto3",
            "uploadphoto4",
            "uploadphoto5",
            "get_uploadphoto1",
            "get_uploadphoto2",
            "get_uploadphoto3",
            "get_uploadphoto4",
            "get_uploadphoto5"

        )

class GuardianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "fullname",
            "username",
            "profilephoto",
            "get_profilephoto",
            "get_absolute_url",
            "get_igAccount",
            "get_fbAccount",
            "phonenumber",
            "dateofbirth",
            "age",
            "gender",
            "occupation",
            "HasPet",
            "petcounter",
            "aboutme",
            "preferredcity",
            "igAccount",
            "fbAccount",
        )

