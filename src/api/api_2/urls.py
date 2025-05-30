from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'locations', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
