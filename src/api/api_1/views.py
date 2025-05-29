from rest_framework import viewsets
from main.models import Event
from .serializers import EventSerializer
from main.api.permissions import IsAuthenticatedUser

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedUser]
