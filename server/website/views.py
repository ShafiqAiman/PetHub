from django.db.models import Q
from django.http import Http404
from django.http.response import HttpResponse, JsonResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import Pet, UserProfile
from .serializers import PetSerializer, HousemateSerializer

class HouseList(viewsets.ModelViewSet):
    
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class HousemateList(viewsets.ModelViewSet):
    
    
    queryset = UserProfile.objects.all()
    serializer_class = HousemateSerializer


class HouseDetail(APIView):
   
    def get_object(self, house_slug):
        try:
            return Pet.objects.get(id=house_slug)
        except Pet.DoesNotExist:
            raise Http404
    
    def get(self, request, house_slug, format=None):
        house = self.get_object(house_slug)
        serializer = PetSerializer(house)
        return Response(serializer.data)


class HousemateDetail(APIView):
    
    def get_object(self, housemate_slug):
        try:
            return UserProfile.objects.get(username=housemate_slug)
        except UserProfile.DoesNotExist:
            raise Http404
    
    def get(self, request, housemate_slug, format=None):
        housemate = self.get_object(housemate_slug)
        serializer = HousemateSerializer(housemate)
        return Response(serializer.data)

