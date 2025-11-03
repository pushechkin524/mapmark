from rest_framework.routers import DefaultRouter
from .views import MarkerViewSet

router = DefaultRouter()
router.register(r'markers', MarkerViewSet)
urlpatterns = router.urls
