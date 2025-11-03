from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# 👇 добавляем импорт секретного вью
from markers.views import SecretAdminView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('markers.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    # 🔐 Секретная страница для удаления меток
    path('supermapmarks123/', SecretAdminView.as_view(), name='admin_map'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
