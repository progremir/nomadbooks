from allauth.account.views import email_verification_sent
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from swagger_render.views import SwaggerUIView

v1 = ([
            path('auth/', include('users.urls'))
      ], 'v1')

urlpatterns = [
    path('email-sent/', email_verification_sent, name='account_email_verification_sent'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1)),
    path('swagger/', SwaggerUIView.as_view()),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.DOCS_URL, document_root=settings.DOCS_ROOT)
