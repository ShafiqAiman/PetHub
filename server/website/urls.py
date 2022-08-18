from django.urls import path, include

from website import views

from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'djangohousemates', views.HousemateList)
router.register(r'djangohouses', views.HouseList)

urlpatterns = [
    
    path('djangohouse/<slug:house_slug>/', views.HouseDetail.as_view()),
    path('djangohousemate/<slug:housemate_slug>/', views.HousemateDetail.as_view()),
    path('', include(router.urls)),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

