from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from swagger_render.views import SwaggerUIView

from django.conf import settings

v1 = ([
      ], 'v1')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1)),
    path('swagger/', SwaggerUIView.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.DOCS_URL, document_root=settings.DOCS_ROOT)
