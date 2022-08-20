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
from .serializers import PetSerializer, GuardianSerializer

class PetList(viewsets.ModelViewSet):
    
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class GuardianList(viewsets.ModelViewSet):
    
    
    queryset = UserProfile.objects.all()
    serializer_class = GuardianSerializer


class PetDetail(APIView):
   
    def get_object(self, pet_slug):
        try:
            return Pet.objects.get(id=pet_slug)
        except Pet.DoesNotExist:
            raise Http404
    
    def get(self, request, pet_slug, format=None):
        house = self.get_object(pet_slug)
        serializer = PetSerializer(house)
        return Response(serializer.data)


class GuardianDetail(APIView):
    
    def get_object(self, guardian_slug):
        try:
            return UserProfile.objects.get(username=guardian_slug)
        except UserProfile.DoesNotExist:
            raise Http404
    
    def get(self, request, guardian_slug, format=None):
        housemate = self.get_object(guardian_slug)
        serializer = GuardianSerializer(housemate)
        return Response(serializer.data)

