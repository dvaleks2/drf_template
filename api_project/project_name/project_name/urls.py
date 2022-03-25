import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from project_name import settings

from users.permissions import IsAdmin

ALLOW_DEV_SWAGGER_LOGIN = True

swagger_permissions = AllowAny if settings.DEBUG else IsAdmin

schema_view = get_schema_view(
    openapi.Info(
        title="Project API",
        default_version='v1',
        description="drf project",
        # terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(swagger_permissions,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include([
        path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        # path('v1/', include([
        #     path('users/', include('users.urls')),
        # ]))
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                   + [(path('__debug__/', include(debug_toolbar.urls)))]

if ALLOW_DEV_SWAGGER_LOGIN:
    urlpatterns += [path('api-auth/', include('rest_framework.urls'))]
