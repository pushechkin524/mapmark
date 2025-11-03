from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Marker
from .serializers import MarkerSerializer

@method_decorator(csrf_exempt, name="dispatch")
class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all().prefetch_related("photos")
    serializer_class = MarkerSerializer
    permission_classes = [AllowAny]
