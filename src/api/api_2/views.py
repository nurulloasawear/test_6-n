from rest_framework import viewsets
from main.models import Location
from .serializers import LocationSerializer
from main.api.permissions import IsAuthenticatedUser

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedUser]
