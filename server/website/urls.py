from django.urls import path, include

from website import views

from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'api/pets', views.PetList)
router.register(r'api/guardians', views.GuardianList)


urlpatterns = [
    
    path('api/pet/<slug:pet_slug>/', views.PetDetail.as_view()),
    path('api/guardian/<slug:guardian_slug>/', views.GuardianDetail.as_view()),
    path('', include(router.urls)),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

