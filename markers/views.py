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

from django.views.generic import TemplateView
from django.http import HttpResponseForbidden

class SecretAdminView(TemplateView):
    template_name = 'admin_map.html'

    def dispatch(self, request, *args, **kwargs):
        key = request.GET.get('key')
        if key != 'ilovecoffee123':  # твой секретный ключ
            return HttpResponseForbidden("Доступ запрещён 😎")
        return super().dispatch(request, *args, **kwargs)

